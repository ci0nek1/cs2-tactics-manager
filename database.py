import sqlite3

DB_NAME = "cs2_tactics.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS economy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tactics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            map_id INTEGER,
            side_id INTEGER,
            economy_id INTEGER,
            description TEXT NOT NULL,
            FOREIGN KEY (map_id) REFERENCES maps(id),
            FOREIGN KEY (side_id) REFERENCES sides(id),
            FOREIGN KEY (economy_id) REFERENCES economy(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Baza danych została pomyślnie zainicjalizowana.")