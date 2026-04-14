import sys
# Importujemy funkcje do obsługi bazy danych z pliku crud.py
from crud import get_id, get_random_tactic

# Predefiniowane listy opcji dostępnych w grze
MAPS = ["Mirage", "Inferno", "Nuke", "Dust II", "Ancient", "Anubis", "Train"]
SIDES = ["CT", "T"]
ECONOMY = ["Pistol round", "Eco round", "Half buy", "Full buy"]


def get_choice(options, prompt):
    """
    Funkcja pomocnicza do wyświetlania menu i pobierania wyboru od użytkownika.
    """
    # Pętla działa dopóki użytkownik nie dokona prawidłowego wyboru
    while True:
        # Wyświetla nagłówek/pytanie (np. "Wybierz mapę:")
        print(f"\n{prompt}")

        # Wyświetla wszystkie dostępne opcje ponumerowane od 1
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        print("0. Wyjście / Powrót")

        # Pobiera dane wpisane przez użytkownika
        choice = input("Twój wybór: ")

        # Opcja 0 służy do wyjścia z programu lub cofnięcia do poprzedniego menu
        if choice == '0':
            return None

        # Próbujemy zamienić wpisaną wartość na liczbę całkowitą
        try:
            idx = int(choice) - 1
            # Sprawdzamy, czy wpisany numer mieści się w zakresie dostępnych opcji
            if 0 <= idx < len(options):
                return options[idx]
            else:
                print("\n[BŁĄD] Nieprawidłowy wybór. Spróbuj ponownie.")
        except ValueError:
            # Komunikat błędu, jeśli użytkownik wpisał tekst zamiast liczby
            print("\n[BŁĄD] Proszę wpisać cyfrę.")


def main():
    """
    Główna funkcja zawierająca pętlę i logikę programu.
    """
    # Główna pętla programu - pozwala na wielokrotne losowanie taktyk
    while True:
        print("\n" + "=" * 30)
        print("=== CS2 Strat Roulette Pro ===")
        print("=" * 30)

        # 1. KROK: Wybór mapy
        selected_map = get_choice(MAPS, "Wybierz mapę:")
        if not selected_map:
            # Jeśli w pierwszym menu wybrano '0', zamykamy całkowicie program
            print("Wychodzenie z programu... GG!")
            sys.exit(0)

        # 2. KROK: Wybór strony (CT/T)
        selected_side = get_choice(SIDES, f"Wybrano: {selected_map}. Wybierz stronę:")
        if not selected_side:
            # Jeśli wybrano '0', wracamy na sam początek (do wyboru mapy)
            continue

        # 3. KROK: Wybór ekonomii
        selected_eco = get_choice(ECONOMY, f"Wybrano: {selected_map} | {selected_side}. Wybierz ekonomię:")
        if not selected_eco:
            # Jeśli wybrano '0', wracamy na sam początek (do wyboru mapy)
            continue

        print("\n" + "*" * 50)
        print(f" GENEROWANIE TAKTYKI: {selected_map} | {selected_side} | {selected_eco}")
        print("*" * 50)

        # Pobieramy unikalne numery ID dla wybranych opcji z bazy danych
        map_id = get_id('maps', selected_map)
        side_id = get_id('sides', selected_side)
        eco_id = get_id('economy', selected_eco)

        # Losujemy taktykę z bazy danych na podstawie pobranych ID
        tactic = get_random_tactic(map_id, side_id, eco_id)

        # Wyświetlamy wylosowaną taktykę lub komunikat o jej braku
        if tactic:
            print(f"\n[ OPIS TAKTYKI ]:\n\n{tactic}")
        else:
            print("\n[ BŁĄD ]: Brak taktyki dla zadanych kryteriów w bazie danych.")

        print("\n" + "*" * 50)
        # Zatrzymuje działanie programu, dopóki gracz nie wciśnie ENTER
        input("Naciśnij [ENTER], aby wylosować kolejną taktykę...")


if __name__ == "__main__":
    main()