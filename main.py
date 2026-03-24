import random
from pymongo import MongoClient

class TacticsManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="cs2_tactics", collection_name="tactics"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.ensure_db_exists()

    def ensure_db_exists(self):
        # Jeśli baza jest pusta, dodaj przykładowe dane
        if self.collection.count_documents({}) == 0:
            sample_entries = [
                {
                    "id": 1, "map": "Mirage", "category": "Tactic", "side": "T", "economy": "Full",
                    "title": "Split A", "description": "Szybki wjazd na A.", "url": "link_do_yt"
                },
                {
                    "id": 2, "map": "Mirage", "category": "Grenade", "type": "Smoke", "side": None, "economy": None,
                    "title": "Window smoke", "description": "Celuj w antenę.", "url": "link_do_zdjecia"
                }
            ]
            self.collection.insert_many(sample_entries)

    def list_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_next_id(self):
        last_entry = self.collection.find_one(sort=[("id", -1)])
        if last_entry and "id" in last_entry:
            return last_entry["id"] + 1
        return 1

    def add_entry(self, entry):
        if not entry.get("id"):
            entry["id"] = self.get_next_id()

        self.collection.insert_one(entry.copy())
        return entry
