import sqlite3


def create_table_cards():
    conn = sqlite3.connect("bussiness_cards.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(60), email VARCHAR(60), age INTEGER, phone VARCHAR(10), additional TEXT)")
    conn.commit()
    conn.close()


def add():
    name = input("Enter user name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    phone = input("Enter Phone: ")
    text_info = input("Enter additional info: ")

    con = sqlite3.connect("bussiness_cards.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO cards (name,email,age,phone,additional) VALUES ('{name}','{email}',{age},'{phone}','{additional}')".format(
        name=name, email=email, age=age, phone=phone, additional=text_info))
# INSERT .... VALUES (Mitko, 2, 3)
    con.commit()

    con.close()


def list():
    con = sqlite3.connect("bussiness_cards.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM cards")
    print(cursor.fetchall())
    con.close()


def delete():
    conn = sqlite3.connect("bussiness_cards.db")
    cursor = conn.cursor()
    id_to_del = input("Enter id to delete: ")

    cursor.execute("DELETE FROM cards WHERE id={id}".format(id=id_to_del))
    conn.commit()
    conn.close()


def get():
    conn = sqlite3.connect("bussiness_cards.db")
    cursor = conn.cursor()
    id_to_get = input("Enter id to get: ")

    cursor.execute("SELECT * FROM cards WHERE id={id}".format(id=id_to_get))
    print(cursor.fetchone())
    conn.commit()
    conn.close()


def help():
    print("###Options###")
    print("#############")
    print("1. `add` - insert new business card")
    print("2. `list` - list all business cards")
    print("3. `delete` - delete a certain business card")
    print("4. `get` -display full information for a certain business card(`ID` is required)")
    print("5. `help` - list all available options")


def main():
    options = {
    'add' : add,
    'list' : list,
    'delete': delete,
    'get': get,
    'help': help}
    create_table_cards()
    help()
    while True:
        option = input("Pick option: ")
        options[option]()

if __name__ == '__main__':
    main()
