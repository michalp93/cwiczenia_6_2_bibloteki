# Import modułów
# Moduły importujemy poleceniem
#       import <nazwa-modułu>
# Lub
#       import<nazwa_moduły> as <alias>

# Przykład, który wyświetli listę katalogów, jak w cmd systemu
# import os
# os.system("dir")


# Uzyskiwanie określonych funkcji z modułu
# from module import <obiekt1>, <obiekt2>, <obiekt3>

# Przykład,Uzyskiwanie określonych funkcji z modułu
# program wypisze "Dobranoc", poczeka 2 sekundy i wypisze "Dzień dobry"

# from time import sleep
# print("Dobranoc")
# sleep(2)
# print("Dzień dobry")


# możliwe jest importowanie wielu (wszystkich) funkcji z modułów
# from module import *
# nie robi się tego gdyż w innej bibliotece mogą występować fukncje o tej samej nazwie!!!


# Dostępność obiektów z załadowanych modułów
# Czyli jak sprawdzić jakie funkcje sa w danym module
# import os
# print(dir(os))     # to nie jest ten dir co w windowsie!!!


# ---------------------------------------Cwiczenie1----------------------------------------
# Zaimportuj moduł matematyczny i wywołaj funkcję sinusoidalną.
# import math
# print(math.sin(0))


# Tworzenie modułów
# import fruit
# # from fruit import lemon
#
# fruit.lemon(5)
# # lemon(5)


# Wyszukiwanie modułów, najpierw szuka je w bierzącym katalogu, później pythonpath zmiennej
# systemowej, później w path


# Instalowanie dodatkowych modułów
# Głównie robi się to przez stronę Python Package Index inaczej zwane jako Cheese Shop

# pip search <paczka>
# instalacja
# pip install <paczka>

# Inna opcja to Conda





