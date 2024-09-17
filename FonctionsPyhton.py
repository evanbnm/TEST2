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
        return (revenu - 10226) * 0.11
    if revenu <= 74545:
        return (revenu - 26071) * 0.3 + (26070 - 10225) * 0.11
    if revenu <= 160336:
        return (revenu - 74546) * 0.41 + (74545 - 26071) * 0.3 + (26070 - 10225) * 0.11
    if revenu > 160336:
        return (revenu - 160337) * 0.45 + (160336 - 74546) * 0.41 + (74545 - 26071) * 0.3 + (26070 - 10225) * 0.11
    return "Revenu invalide"
   

        
    




    