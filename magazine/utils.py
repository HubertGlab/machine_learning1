class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_1 = sum(self.marks) / len(self.marks)
        if marks_1 > 3:
            return True
        else:
            return False


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"{self.city}|{self.street}|{self.zip_code}|{self.open_hours}|{self.phone}|"


class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name}|{self.last_name}|{self.hire_date}|{self.birth_date}|" \
               f"{self.city}|{self.street}|{self.zip_code}|{self.phone}|"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka z +{self.publication_date} autora {self.author_name} {self.author_surname} " \
               f"Mająca {self.number_of_pages} stron"


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Zamówienie obsługiwane przez {self.employee} Zamówione przez {self.student} " \
               f"Zawierające {str(str([ksiazka]) for ksiazka in self.books)} o dacie {self.order_date}"


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot, rozmair_dzialki: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        self.rozmiar_dzialki = rozmair_dzialki

    def __str__(self):
        return f'House with area of {self.area} and {self.rooms} rooms, costs {self.price}' \
               f', in {self.address}, plot {self.plot}, area {self.rozmiar_dzialki}'


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat with area of {self.area} and {self.rooms} rooms, costs {self.price}' \
               f', in {self.address}, on {self.floor} floor'






