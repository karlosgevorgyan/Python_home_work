from model.Address import Address
from model.User import User
from model.Book import Book
import random

def generate_addresses(count):
    addresses = list()
    countries = ['Country' + str(i) for i in range(count // 10)]
    cities = ['City' + str(i) for i in range(len(countries) * 2)]
    zip_codes = [str(zip_code) for zip_code in range(1000, 1015)]
    streets = ['Street' + str(i) for i in range(50)]
    for i in range(1, count + 1):
        address_id = i
        country = random.choice(countries)
        city = random.choice(cities)
        zip_code = random.choice(zip_codes)
        street = random.choice(streets)
        address = Address(address_id, country, city, street, zip_code, i)
        addresses.append(address)
    return addresses


def generate_users(addresses, count):
    users = list()
    names = ['Names' + str(i) for i in range(count // 10)]
    surnames = ['Surnames' + str(i) for i in range(len(names) * 2)]
    genders = ['Male', 'Female']
    for i in range(1, count + 1):
        user_id = i
        name = random.choice(names)
        surname = random.choice(surnames)
        gender = random.choice(genders)
        age = i
        address = random.choice(addresses)
        user = User(user_id, name, surname, age, gender, address, None)
        users.append(user)
    return users


def generate_books(count):
    books = list()
    authors = ['Author' + str(i) for i in range(count)]
    for i in range(1, count + 1):
        book_id = i
        author = random.choice(authors)
        title = 'Title' + str(i)
        description = 'Description' + str(i)
        chapter_count = i
        page_count = i * 10
        book = Book(book_id, author, title, description, chapter_count, page_count)
        books.append(book)
    return books


def generate_books_data_and_save_into_file(count):
    books = generate_books(count)
    write_to_file(books, 'raw/books.csv')
    return books


def generate_addresses_data_and_save_into_file(count):
    addresses = generate_addresses(count)
    write_to_file(addresses, 'raw/addresses.csv')
    return addresses


def generate_users_data_and_save_into_file(addresses, count):
    users = generate_users(addresses, count)
    write_to_file(users, 'raw/users.csv')
    return users


def generate_users_books_and_save_into_file(users, books):
    data = list()
    for u in users:
        user_id = u.user_id
        for b in books:
            book_id = b.book_id
            data.append(str(user_id) + ',' + str(book_id))
    write_to_file(data, 'raw/users_books.csv')


def write_to_file(data, file_path):
    with open(file_path, 'w') as f:
        for d in data:
            f.write(str(d) + '\n')


def generate_data():
    addresses = generate_addresses_data_and_save_into_file(100)
    users = generate_users_data_and_save_into_file(addresses, 1000)
    books = generate_books_data_and_save_into_file(10)
    generate_users_books_and_save_into_file(users, books)
