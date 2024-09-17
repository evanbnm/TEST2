# coding : utf-8
'''
TP 1 PYTHON
@ Evan Benhamou
Date : 17/09/2024

Ce programme est une liste de fonctions utilisées dans le programme Exo1.py
'''

def TestBissextile(annee):
    """
    Vérifie si une année est bissextile
    entrée : année
    sortie : booléen
    """
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def NbJoursMois(mois, annee):
    '''
    Donne le nombre de jour dans un mois en fonction de l'année
    entrée : mois, annee
    sortie : nombre de jours
    '''
    trente_et_un = [1, 3, 5, 7, 8, 10, 12] 
    trente = [4, 6, 9, 11]
    if mois in trente_et_un:
        return 31
    elif mois in trente:
        return 30
    elif mois == 2:
        if TestBissextile(annee):
            return 29
        else:
            return 28
    else:
        return "Mois invalide"
    
def DateValide(jour, mois, annee):
    '''
    Vérifie si une date est valide
    entrée : jour, mois, annee
    sortie : Date valide ou invalide
    '''
    if mois < 1 or mois > 12:
        return "Date invalide"
    if jour < 1 or jour > NbJoursMois(mois, annee):
        return "Date invalide"
    return "Date valide"

def mesImpots(revenu):
    '''
    Calcule le montant de l'impôt sur le revenu
    entrée : revenu
    sortie : montant de l'impôt
    '''
    if revenu <= 10225:
        return 0
    if revenu <= 26070:
        return int((revenu - 10226) * 0.11)
    if revenu <= 74545:
        return int((revenu - 26071) * 0.3 + (26070 - 10225) * 0.11)
    if revenu <= 160336:
        return int((revenu - 74546) * 0.41 + (74545 - 26071) * 0.3 + (26070 - 10225) * 0.11)
    if revenu > 160336:
        return int((revenu - 160337) * 0.45 + (160336 - 74546) * 0.41 + (74545 - 26071) * 0.3 + (26070 - 10225) * 0.11)
    return "Revenu invalide"

def multiplication(a, b):
    '''
    Multiplie deux matrices
    entrée : a, b
    sortie : a * b
    '''
    if len(a[0]) != len(b):
        return "Matrices incompatibles"
    
    C = []

    for i in range(len(a)):
        C.append([])
        for j in range(len(b[0])):
            C[i].append(0)
            for k in range(len(b)):
                C[i][j] += a[i][k] * b[k][j]
    return C

def hanoi(n, A, B, C):
    '''
    Résout le problème des tours de Hanoï
    entrée : n, A, B, C
    sortie : déplacement des disques
    '''
    if n == 1:
        print("Déplacer le disque 1 de", A, "à", C)
        return
    hanoi(n-1, A, C, B)
    print("Déplacer le disque", n, "de", A, "à", C)
    hanoi(n-1, B, A, C)


 





   
   

        
    




    