# Code Academy 4: Przetwarzanie danych
# 			  put.NET junior
# ______________________________________
# 				   2016
# ______________________________________

import csv

price = 450
counter = 0

# Otworz plik 04_dane.csv
with open('04_dane.csv') as csvfile:
    # Parsuj zawartosc do slownika
    reader = csv.DictReader(csvfile)

    for row in reader:
        # sprawdz czy kolumna ocena, 
        # rzutowana do typu zmiennoprzecinkowego float
        # jest równa 2
        if float(row['ocena']) == 2:
            counter += 1

# Pomnoz cene przez ilosc i rzutuj do typu tekstowego str
print(str(price * counter) + " zl")