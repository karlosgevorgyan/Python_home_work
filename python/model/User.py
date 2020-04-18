class User:

    def __init__(self, user_id, name, surname, age, gender, address, books):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.address = address
        self.books = books

    def __str__(self):
        return ','.join([str(self.user_id), self.name, self.surname, str(self.age),
                         self.gender, str(self.address.address_id)])

    def __eq__(self, other):
        return self.user_id == other.user_id \
               and self.name == other.name \
               and self.surname == other.surname \
               and self.age == other.age \
               and self.gender == other.gender \
               and self.address == other.address

    def __ne__(self, other):
        return not self == other
