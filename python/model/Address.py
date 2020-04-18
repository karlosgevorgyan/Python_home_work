class Address:

    def __init__(self, address_id, country, city, street, zip_code, street_number):
        self.address_id = address_id
        self.city = city
        self.country = country
        self.zip_code = zip_code
        self.street = street
        self.street_number = street_number

    def __str__(self):
        return ','.join([str(self.address_id), self.country, self.city, self.street,
                         self.zip_code, str(self.street_number)])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.address_id == other.address_id \
               and self.country == other.country \
               and self.city == other.city \
               and self.street == other.street \
               and self.zip_code == other.zip_code \
               and self.street_number == other.street_number

    def __ne__(self, other):
        return not self == other
