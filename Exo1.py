# coding: utf-8

import FonctionsPyhton as f

# annee = int(input("Saisissez une année : "))
# print(f.TestBissextile(annee))

# mois = int(input("Saisissez un mois : "))
# print(f.NbJoursMois(mois, annee))

# jour = int(input("Saisissez un jour : "))
# print(f.DateValide(jour, mois, annee))

# date = input("Saisissez une date (jj/mm/aaaa) : ").split("/")
# jour, mois, annee = int(date[0]), int(date[1]), int(date[2])
# print(f.DateValide(jour, mois, annee))

# revenu = int(input("Saisissez votre revenu : "))
# print(f.mesImpots(revenu))

# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# B = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# print("C = ")
# for row in f.multiplication(A, B):
#     print(row)

f.hanoi(3, "A", "B", "C")