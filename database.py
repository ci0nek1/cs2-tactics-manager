import sqlite3

DB_NAME = "cs2_tactics.db"

def get_connection():
    return sqlite3.connect(DB_NAME)