from database import get_connection

def insert_dictionary_item(table_name, item_name):
    conn = get_connection()
    try:
        conn.execute(f'INSERT OR IGNORE INTO {table_name} (name) VALUES (?)', (item_name,))
        conn.commit()
    finally:
        conn.close()

def get_id(table_name, item_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT id FROM {table_name} WHERE name = ?', (item_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def insert_tactic(map_name, side_name, economy_name, description):
    map_id = get_id('maps', map_name)
    side_id = get_id('sides', side_name)
    economy_id = get_id('economy', economy_name)

    if not all([map_id, side_id, economy_id]):
        print(f"Błąd dodawania taktyki. Sprawdź nazwy: {map_name}, {side_name}, {economy_name}")
        return

    conn = get_connection()
    try:
        conn.execute('''
            INSERT INTO tactics (map_id, side_id, economy_id, description)
            VALUES (?, ?, ?, ?)
        ''', (map_id, side_id, economy_id, description))
        conn.commit()
    finally:
        conn.close()

def get_random_tactic(map_id, side_id, economy_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT description FROM tactics
        WHERE map_id = ? AND side_id = ? AND economy_id = ?
        ORDER BY RANDOM() LIMIT 1
    ''', (map_id, side_id, economy_id))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None