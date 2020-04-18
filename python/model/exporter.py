import .connecotr
def open_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Test1234!",
        database="Test"
    )


def load_addresses_and_save_into_file(cursor):
    query = "select * from address;"
    cursor.execute(query)
    addresses = cursor.fetchall()
    save_into_file(addresses, 'dump/addresses.csv')


def load_users_and_save_into_file(cursor):
    query = "select * from user;"
    cursor.execute(query)
    users = cursor.fetchall()
    save_into_file(users, 'dump/users.csv')


def load_books_and_save_into_file(cursor):
    query = "select * from book;"
    cursor.execute(query)
    books = cursor.fetchall()
    save_into_file(books, 'dump/books.csv')


def load_users_books_and_save_into_file(cursor):
    query = "select * from user_book;"
    cursor.execute(query)
    users_books = cursor.fetchall()
    save_into_file(users_books, 'dump/users_books.csv')


def save_into_file(data, file_name):
    with open(file_name, 'w') as f:
        for d in data:
            f.write(','.join([str(el) for el in d]) + '\n')


def export_data():
    connection = open_connection()
    cursor = connection.cursor()
    load_addresses_and_save_into_file(cursor)
    load_users_and_save_into_file(cursor)
    load_books_and_save_into_file(cursor)
    load_users_books_and_save_into_file(cursor)
    cursor.close()
