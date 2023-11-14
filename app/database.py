import sqlite3 as sq

db = sq.connect('authentication.db')
cur = db.cursor()

def delete_login_and_password():
    cur.execute("DELETE FROM auth")
    db.commit()

def get_login():
    cur.execute("SELECT login FROM auth")
    result = cur.fetchone()
    return result[0] if result else None
    
def get_password():
    cur.execute("SELECT password FROM auth")
    result = cur.fetchone()
    return result[0] if result else None

def login_and_password_input():
    while True:
        log = get_login()
        pas = get_password()
        if log is None and pas is None:
            login = input('Enter the login from the Twin cabinet: ')
            password = input('Enter the password for the Twin cabinet: ')
            if not login or not password:
                print("Both login and password are required. Please try again.")
            else:
                return login, password
        else:
            return log, pas

def db_auth():
    data = cur.fetchone()
    if not data:
        login, password = login_and_password_input()
        cur.execute("INSERT INTO auth VALUES(?,?)",(login, password))
        db.commit()
    else:
        return False
    
def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS auth("
                "login TEXT, "
                "password TEXT )")
    db.commit()