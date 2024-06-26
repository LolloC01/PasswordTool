import sqlite3
import pathlib


PATH_DB = r"C:\Users\lorya\ElectronProjects\PasswordManager\data\PasswordManager.db"

class DBContextManager:

    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.connection = None

    def check_db(self, path: str) -> bool:
        """Controlla se il database esiste

        Args:
            path (str): percorso del database

        Returns:
            bool:   TRUE -> Il DB esisteù
                    FALSE -> Il DB non esiste
        """
        file_path = pathlib.Path(path)
        if file_path.exists():
            print("Il file esiste!")
            return True
        else:
            print("Il file non esiste!")
            return False

    def connect(self, db):
        """
        Si connette al database
        """
        if self.check_db(PATH_DB):
            self.connection = f"Connessione al database {self.db_name}"
            
        


def db_init() -> None:
    """
    Controlla se il database esiste o no e in caso ne crea uno nuovo
    """
    if not check_db(PATH_DB):

        #creo la connessione al DB
        conn = sqlite3.connect(PATH_DB)

        #creo il cursore
        curs = conn.cursor()

        #Creo la tabella dei profili utente
        curs.execute('''CREATE TABLE User (ID INTEGER PRIMARY KEY,
                     User text,
                     Password text,
                     Email text)''')

        #Creo la tabella delle password
        curs.execute('''CREATE TABLE Password (ID INTEGER PRIMARY KEY,
                    ID_User Integer,
                    Sito text,
                    Username text,
                    Password text,
                    FOREIGN KEY(ID_User) REFERENCES User(ID))''')
        conn.commit()

        curs.close()

        conn.close()


db_init()

def add_user(email, username, password, id_user) -> list:
    #creo la connessione al DB
    conn = sqlite3.connect(PATH_DB)

    #creo il cursore
    curs = conn.cursor()

    #Creo la tabella dei profili utente
    curs.execute(f'''INSERT INTO User (ID, User, Password, Email) VALUES (?,?,?,?)''',(id_user,username,password,email))

    #commit
    conn.commit()

    #chiudo il cursore
    curs.close()

    #chiudo la connessione al database
    conn.close()

def add_user(sito, username, password, id_user, id) -> list:
    #creo la connessione al DB
    conn = sqlite3.connect(PATH_DB)

    #creo il cursore
    curs = conn.cursor()

    #Creo la tabella dei profili utente
    curs.execute(f'''INSERT INTO User (ID, ID_User, Sito, Username, Password) VALUES (?,?,?,?,?)''',(id, id_user, sito, username, password))

    #commit
    conn.commit()

    #chiudo il cursore
    curs.close()

    #chiudo la connessione al database
    conn.close()


def get_from_db(table, filter):
    #creo la connessione al DB
    conn = sqlite3.connect(PATH_DB)

    #creo il cursore
    curs = conn.cursor()

    #Creo la tabella dei profili utente
    curs.execute(f'''FROM {table} GET
    #commit
    conn.commit()

    #chiudo il cursore
    curs.close()

    #chiudo la connessione al database
    conn.close()
