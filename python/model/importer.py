
import mysql.connector

def open_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Test1234!",
        database="test"
    )



def load_users_books_and_save_into_db(cursor):
    with open('raw/users_books.csv', 'r') as f:
        users_books = f.readlines()
    query = """
        insert into user_book(user_id, book_id) 
        values(%s, %s);
    """
    for ub in users_books:
        cursor.execute(query, ub.strip().split(','))


def load_books_and_save_into_db(cursor):
    with open('raw/books.csv', 'r') as f:
        books = f.readlines()
    query = """
        insert into book(id, author, title, description, chapter_count, page_count) 
        values(%s, %s, %s, %s, %s, %s);
    """
    for b in books:
        cursor.execute(query, b.strip().split(','))


def load_address_and_save_into_db(cursor):
    with open('raw/addresses.csv', 'r') as f:
        addresses = f.readlines()
    query = """
        insert into address(id, country, city, street, zip_code, street_number) 
        values(%s, %s, %s, %s, %s, %s);
    """
    for address in addresses:
        cursor.execute(query, address.strip().split(','))


def load_users_and_save_into_db(cursor):
    with open('raw/users.csv', 'r') as f:
        users = f.readlines()
    query = """
        insert into user(id, name, surname, age, gender, address_id) 
        values(%s, %s, %s, %s, %s, %s);
    """
    for u in users:
        cursor.execute(query, u.strip().split(','))

def import_data():
    connection = open_connection()

    cursor = connection.cursor()
    try:
        load_address_and_save_into_db(cursor)
        load_books_and_save_into_db(cursor)
        load_users_and_save_into_db(cursor)
        load_users_books_and_save_into_db(cursor)
        connection.commit()
        cursor.close()
    except Exception as e:
        connection.rollback()
        print(e)
