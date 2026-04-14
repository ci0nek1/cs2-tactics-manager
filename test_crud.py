import unittest
from unittest.mock import patch
import sqlite3
import os
import crud  # Twój plik


# Zwykła funkcja, która łączy się z naszym specjalnym testowym plikiem
def get_test_connection():
    return sqlite3.connect('testowa_baza_cs2.db')


class TestCRUDWithTempDB(unittest.TestCase):

    # setUp odpala się automatycznie PRZED każdym pojedynczym testem
    def setUp(self):
        # 1. Tworzymy fizyczny plik bazy testowej i strukturę tabel
        conn = get_test_connection()
        conn.execute('CREATE TABLE maps (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
        conn.execute('CREATE TABLE sides (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
        conn.execute('CREATE TABLE economy (id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
        conn.execute('''
                     CREATE TABLE tactics
                     (
                         id          INTEGER PRIMARY KEY,
                         map_id      INTEGER,
                         side_id     INTEGER,
                         economy_id  INTEGER,
                         description TEXT
                     )
                     ''')
        conn.commit()
        conn.close()

    # tearDown odpala się automatycznie PO każdym pojedynczym teście
    def tearDown(self):
        # 2. Usuwamy plik bazy testowej, żeby każdy test miał absolutnie czystą kartę
        if os.path.exists('testowa_baza_cs2.db'):
            # W systemie Windows plik może być jeszcze przez ułamek sekundy zablokowany,
            # więc upewniamy się, że został puszczony i kasujemy.
            try:
                os.remove('testowa_baza_cs2.db')
            except PermissionError:
                pass

    # Tutaj MOCKUJEMY tylko miejsce, do którego się łączymy.
    # Mówimy: zamiast crud.get_connection używaj naszej funkcji get_test_connection
    @patch('crud.get_connection', side_effect=get_test_connection)
    def test_insert_dictionary_item(self, mock_conn):

        # WYKONUJEMY TWOJĄ FUNKCJĘ
        crud.insert_dictionary_item('maps', 'Inferno')

        # SPRAWDZAMY W PRAWDZIWEJ BAZIE, CZY TO ZADZIAŁAŁO
        conn = get_test_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM maps WHERE name = 'Inferno'")
        wynik = cursor.fetchone()
        conn.close()

        # Sprawdzamy czy pobrany wynik to ('Inferno',)
        self.assertIsNotNone(wynik, "Mapa nie zapisała się w bazie!")
        self.assertEqual(wynik[0], 'Inferno')

    @patch('crud.get_connection', side_effect=get_test_connection)
    def test_get_id(self, mock_conn):
        # Najpierw ręcznie "wstrzykujemy" coś do bazy testowej
        conn = get_test_connection()
        conn.execute("INSERT INTO sides (name) VALUES ('CT')")
        conn.commit()
        conn.close()

        # Sprawdzamy czy funkcja get_id poprawnie to znajdzie (powinno dostać ID = 1)
        wynik = crud.get_id('sides', 'CT')
        self.assertEqual(wynik, 1)

    @patch('crud.get_connection', side_effect=get_test_connection)
    def test_insert_tactic(self, mock_conn):
        # Najpierw dodajemy słowniki przy pomocy twojej funkcji
        crud.insert_dictionary_item('maps', 'Nuke')
        crud.insert_dictionary_item('sides', 'T')
        crud.insert_dictionary_item('economy', 'Pistol round')

        # Wywołujemy główną funkcję dodawania taktyki
        crud.insert_tactic('Nuke', 'T', 'Pistol round', 'Rash B no stop')

        # Odpytujemy bazę testową czy taktyka fizycznie tam siedzi
        conn = get_test_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM tactics")
        wynik = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(wynik, "Taktyka nie dodała się do bazy!")
        self.assertEqual(wynik[0], 'Rash B no stop')


if __name__ == '__main__':
    unittest.main()