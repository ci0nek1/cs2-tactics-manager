import unittest
from unittest.mock import patch
import sys

# Importujemy funkcje i stałe z twojego głównego pliku (zakładamy, że to main.py)
from main import get_choice, main, MAPS


class TestCS2StratRoulette(unittest.TestCase):

    # 1. Testujemy poprawny wybór z menu
    @patch('builtins.input', side_effect=['1'])  # Symulujemy wpisanie '1' przez użytkownika
    @patch('builtins.print')  # Blokujemy wyświetlanie print() w konsoli podczas testów
    def test_get_choice_valid(self, mock_print, mock_input):
        wynik = get_choice(MAPS, "Wybierz mapę:")
        # Pierwsza opcja na liście MAPS to "Mirage"
        self.assertEqual(wynik, "Mirage")

    # 2. Testujemy wybranie opcji '0' (Wyjście/Powrót)
    @patch('builtins.input', side_effect=['0'])
    @patch('builtins.print')
    def test_get_choice_exit(self, mock_print, mock_input):
        wynik = get_choice(MAPS, "Wybierz mapę:")
        # Oczekujemy, że funkcja zwróci None
        self.assertIsNone(wynik)

    # 3. Testujemy błędne wpisanie liter zamiast cyfry, a potem poprawę
    @patch('builtins.input', side_effect=['abc', '2'])  # Najpierw 'abc', potem '2'
    @patch('builtins.print')
    def test_get_choice_invalid_string_then_valid(self, mock_print, mock_input):
        wynik = get_choice(MAPS, "Wybierz mapę:")
        # Oczekujemy "Inferno" (druga opcja), program powinien zignorować 'abc' i zapytać ponownie
        self.assertEqual(wynik, "Inferno")

    # 4. Testujemy podanie liczby spoza zakresu, a potem poprawę
    @patch('builtins.input', side_effect=['99', '3'])  # Najpierw '99', potem '3'
    @patch('builtins.print')
    def test_get_choice_out_of_range_then_valid(self, mock_print, mock_input):
        wynik = get_choice(MAPS, "Wybierz mapę:")
        # Oczekujemy "Nuke" (trzecia opcja), program powinien zignorować '99'
        self.assertEqual(wynik, "Nuke")

    # 5. Testujemy główną funkcję - co się stanie, gdy użytkownik od razu wpisze 0
    @patch('main.get_choice', return_value=None)  # Symulujemy, że get_choice od razu zwraca None (wybór '0')
    @patch('sys.exit')  # Przechwytujemy sys.exit, żeby test się nie wyłączył
    @patch('builtins.print')
    def test_main_exits_immediately(self, mock_print, mock_exit, mock_get_choice):
        main()
        # Sprawdzamy, czy program faktycznie próbował się zamknąć kodem sys.exit(0)
        mock_exit.assert_called_once_with(0)

    # 6. Testujemy pełne przejście (tzw. "Happy Path") z symulacją bazy danych
    @patch('main.get_choice', side_effect=["Mirage", "CT", "Full buy"])  # Symulujemy przejście przez 3 menu
    @patch('main.get_id', side_effect=[1, 1, 4])  # Symulujemy zwrócenie ID z bazy (crud.get_id)
    @patch('main.get_random_tactic', return_value="Rush B don't stop!")  # Symulujemy wylosowaną taktykę
    @patch(
        'builtins.input', side_effect=[''])  # Symulujemy wciśnięcie ENTER na końcu
    @patch('builtins.print')
    def test_main_full_flow(self, mock_print, mock_input, mock_tactic, mock_get_id, mock_get_choice):
        # Ponieważ w main() jest pętla "while True", musimy ją jakoś zatrzymać, żeby test nie trwał w nieskończoność.
        # Rzucamy specjalny wyjątek po wciśnięciu ENTER
        mock_input.side_effect = KeyboardInterrupt

        with self.assertRaises(KeyboardInterrupt):
            main()

        # Sprawdzamy, czy funkcja losująca taktykę została wywołana z poprawnymi ID
        mock_tactic.assert_called_once_with(1, 1, 4)


if __name__ == '__main__':
    unittest.main()