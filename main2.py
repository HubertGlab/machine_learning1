# 1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
# wyświetlić ( print )
# 2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
# mnożenia obu liczb.
# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"
# 4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
# pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool
# 5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
# . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
# pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.
# 6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.

# 1.

# def funkcja_1 (name: str, surname: str):
#     return "Cześć {0} {1}!".format(name, surname)
#
#
# imie = funkcja_1("Michał", "Anioł")
# print(imie)

# 2.

# def funkcja_2 (liczba: int, liczba2: int):
#     return liczba * liczba2
#
#
# print(funkcja_2(2, 3))

# 3.

# def funkcja_3(liczba: int):
#     if liczba % 2 == 0:
#         return True
#     else:
#         return False
#
#
# liczba_3 = funkcja_3(5)
#
# print("Nieparzysta") if liczba_3 == False else print("Parzysta")

# 4

# def funkcja_4(liczba_1: int, liczba_2: int, liczba_3: int):
#     if (liczba_1 + liczba_2) >= liczba_3:
#         return True
#     else:
#         return False
#
# print(funkcja_4(1, 2, 3))

# 5
# def funkcja_5(lista: list, liczba: int):
#     for licz in lista:
#         if liczba == licz:
#             return True
#
#
# print(funkcja_5([1, 2, 3, 4, 5], 4))

#6

# def funkcja_6(lista_1: list, lista_2: list):
#     final_list = lista_1 + lista_2
#     final_list = list(dict.fromkeys(final_list))
#     return [x ** 3 for x in final_list]
#
#
# print(funkcja_6([1, 2, 3, 4], [2, 3, 6, 10]))
