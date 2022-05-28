import sqlite3

def get_last_guide():
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    print("Last Guide execution")
    cursor.execute("""SELECT * FROM Guides ORDER BY date desc LIMIT 1""")
    data = cursor.fetchone()
    cursor.close()
    return data
def get_all_guides():
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    print("Last Guide execution")
    cursor.execute("""SELECT * FROM Guides ORDER BY date desc""")
    data = cursor.fetchall()
    cursor.close()
    return data

def create(sql_sentence):
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    cursor.execute(sql_sentence)
    sqliteConnection.commit()
    if cursor.rowcount > 0:
        print(f'succesfully created {cursor.rowcount} items')
    # cursor.close()
    return True if cursor.rowcount > 0 else False


def read(sql_sentence, *single):
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    if single:
        print("Single")
        cursor.execute(sql_sentence)
        # cursor.close()
        return cursor.fetchone()
    else:
        print("Multiple")
        cursor.execute(sql_sentence)
        # cursor.close()
        return cursor.fetchall()



def update(sql_sentence):
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    cursor.execute(sql_sentence)
    sqliteConnection.commit()
    if cursor.rowcount > 0:
        print(f'succesfully updated {cursor.rowcount} items')
    # cursor.close()
    return True if cursor.rowcount > 0 else False


def delete(sql_sentence):
    # Connects to DB
    sqliteConnection = sqlite3.connect('schulfDB.sqlite')
    cursor = sqliteConnection.cursor()
    # Print statement and execution
    cursor.execute(sql_sentence)
    sqliteConnection.commit()
    if cursor.rowcount > 0:
        print(f'succesfully deleted {cursor.rowcount} items')
    # cursor.close()
    return True if cursor.rowcount > 0 else False
