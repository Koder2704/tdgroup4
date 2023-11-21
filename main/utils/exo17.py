

def calculer_schtroumpf(tableau1, tableau2):
    schtroumpf = 0
    for element1 in tableau1:
        for element2 in tableau2:
            schtroumpf += element1 * element2
    return schtroumpf

# Exemple d'utilisation
# tableau1 = [1, 2, 3]
# tableau2 = [4, 5, 6]
# resultat_schtroumpf = calculer_schtroumpf(tableau1, tableau2)
# print("Le schtroumpf des deux tableaux est :", resultat_schtroumpf)
