
from model.Address import Address
from model.User import User
from model.Book import Book


def load_addresses(dir):
    addresses = {}
    with open(dir + '/' + 'addresses.csv', 'r') as f:
        str_addresses = f.readlines()
        for str_address in str_addresses:
            address_data = str_address.strip().split(',')
            addresses[address_data[0]] = Address(address_data[0], address_data[1], address_data[2],
                                                 address_data[3], address_data[4], address_data[5])
    return addresses



def load_books(dir):
    books = {}
    with open(dir + '/' + 'books.csv', 'r') as f:
        str_books = f.readlines()
        for str_book in str_books:
            book_data = str_book.strip().split(',')
            books[book_data[0]] = Book(book_data[0], book_data[1], book_data[2],
                                       book_data[3], book_data[4], book_data[5])
    return books


def load_users_books(dir):
    users_books = {}
    with open(dir + '/' + 'users_books.csv', 'r') as f:
        str_users_books = f.readlines()
        for str_user_book in str_users_books:
            user_book_data = str_user_book.strip().split(',')
            if not users_books.get(user_book_data[0]):
                users_books[user_book_data[0]] = list()
            users_books.get(user_book_data[0]).append(user_book_data[1])
    return users_books


def load_users(dir, addresses, books, users_books):
    users = {}
    with open(dir + '/' + 'users.csv', 'r') as f:
        str_users = f.readlines()
        for str_user in str_users:
            user_data = str_user.strip().split(',')
            user_id = user_data[0]
            user_books_ids = users_books.get(user_id)
            user_books = None
            if user_books_ids:
                user_books = [books.get(book_id) for book_id in user_books_ids]
            users[user_id] = (User(user_data[0], user_data[1], user_data[2],
                                   user_data[3], user_data[4],
                                   addresses.get(user_data[5]), user_books))
    return users


def compare_files_content(raw_data, dumped_data):
    for raw_id, raw_obj in raw_data.items():
        dumped_obj = dumped_data.get(raw_id)
        if not dumped_obj or dumped_obj != raw_obj:
            print(raw_id + 'not exist in db')

def compare_data():
    raw_addresses = load_addresses('raw')
    dumped_addresses = load_addresses('dump')
    compare_files_content(raw_addresses, dumped_addresses)
    raw_books = load_books('raw')
    dumped_books = load_books('dump')
    compare_files_content(raw_books, dumped_books)
    raw_users_books = load_users_books('raw')
    dumped_users_books = load_users_books('dump')
    compare_files_content(raw_users_books, dumped_users_books)
    raw_users = load_users('raw', raw_addresses, raw_books, raw_users_books)
    dumped_users = load_users('dump', dumped_addresses, dumped_books, dumped_users_books)
    compare_files_content(raw_users, dumped_users)
