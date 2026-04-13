
import sys
from crud import get_id, get_random_tactic

MAPS = ["Mirage", "Inferno", "Nuke", "Dust II", "Ancient", "Anubis", "Train"]
SIDES = ["CT", "T"]
ECONOMY = ["Pistol round", "Eco round", "Half buy", "Full buy"]


def get_choice(options, prompt):
    while True:
        print(f"\n{prompt}")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        print("0. Wyjście / Powrót")

        choice = input("Twój wybór: ")
        if choice == '0':
            return None

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
            else:
                print("\n[BŁĄD] Nieprawidłowy wybór. Spróbuj ponownie.")
        except ValueError:
            print("\n[BŁĄD] Proszę wpisać cyfrę.")


def main():
    while True:
        print("\n" + "=" * 30)
        print("=== CS2 Strat Roulette Pro ===")
        print("=" * 30)

        selected_map = get_choice(MAPS, "Wybierz mapę:")
        if not selected_map:
            print("Wychodzenie z programu... GG!")
            sys.exit(0)

        selected_side = get_choice(SIDES, f"Wybrano: {selected_map}. Wybierz stronę:")
        if not selected_side:
            continue

        selected_eco = get_choice(ECONOMY, f"Wybrano: {selected_map} | {selected_side}. Wybierz ekonomię:")
        if not selected_eco:
            continue

        print("\n" + "*" * 50)
        print(f" GENEROWANIE TAKTYKI: {selected_map} | {selected_side} | {selected_eco}")
        print("*" * 50)


        map_id = get_id('maps', selected_map)
        side_id = get_id('sides', selected_side)
        eco_id = get_id('economy', selected_eco)


        tactic = get_random_tactic(map_id, side_id, eco_id)

        if tactic:
            print(f"\n[ OPIS TAKTYKI ]:\n\n{tactic}")
        else:
            print("\n[ BŁĄD ]: Brak taktyki dla zadanych kryteriów w bazie danych.")

        print("\n" + "*" * 50)
        input("Naciśnij [ENTER], aby wylosować kolejną taktykę...")


if __name__ == "__main__":
    main()