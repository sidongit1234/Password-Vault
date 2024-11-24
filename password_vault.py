import sqlite3
def create_vault(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS PASSWORDS(
                   id INTEGER PRIMARY KEY
                   service TEXT
                   username TEXT
                   password TEXT 
                   date_added TIMESTAMP
                   )
                   
                   ''')

    conn.commit()
    conn.close()
def main():
    db_file = 'password_vault.db'
 