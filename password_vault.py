import sqlite3
def create_vault(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS PASSWORDS(
                   id INTEGER PRIMARY KEY,

                   service TEXT,

                   username TEXT,

                   password TEXT,

                   date_added TIMESTAMP
            
                   )
                   
                   ''')

    conn.commit()

    conn.close()

def password_vault_menu():

    print("/nPassword Vault Menu")

    print("1. Add password")

    print("2. Remove Password")
          
    print("3. View Password")

    print("4. Change password")

    print("5. Exit")
          

def main():
    db_file = 'password_vault.db'

    create_vault(db_file)

    print("Welcome to the password vault")

    password_vault_menu()
 
if __name__ == "__main__":

    main()