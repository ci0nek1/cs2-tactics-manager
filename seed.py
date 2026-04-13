
from database import init_db
from crud import insert_dictionary_item


MAPS = ["Mirage", "Inferno", "Nuke", "Dust II", "Ancient", "Anubis", "Train"]
SIDES = ["CT", "T"]
ECONOMY = ["Pistol round", "Eco round", "Half buy", "Full buy"]


def seed_base_dictionaries():
    print("Inicjalizacja struktury bazy danych...")
    init_db()

    print("Seedowanie map...")
    for map_name in MAPS:
        insert_dictionary_item('maps', map_name)

    print("Seedowanie stron...")
    for side in SIDES:
        insert_dictionary_item('sides', side)

    print("Seedowanie ekonomii...")
    for eco in ECONOMY:
        insert_dictionary_item('economy', eco)

    print("Słowniki bazowe zostały pomyślnie zapisane w bazie!")


if __name__ == "__main__":
    seed_base_dictionaries()