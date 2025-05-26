import sqlite3
import os

db_path = os.path.join(
    os.path.dirname(
        os.path.dirname(__file__)
    ),
        'Storage.db'
)

conn = None
cursor = None

def open_connection():
    """
    Opens a connection to the SQLite database defined by db_path.
    
    If the connection is already open, it prints a message instead.

    @return None
    """
    global conn, cursor
    if conn is None:
        conn = sqlite3.connect(db_path)
        
        cursor = conn.cursor()
        print("[DB] Connection opened.")
    else:
        print("[DB] Connection already open.")

def close_connection():
    """
    Closes the active SQLite database connection, if one is open.
    
    Resets the global connection variable to None.
    If no connection is open, it prints a message.

    @return None
    """
    global conn
    if conn:
        conn.close()
        conn = None
        print("[DB] Connection closed.")
    else:
        print("[DB] No open connection to close.")