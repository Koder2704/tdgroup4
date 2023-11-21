'''
    Une matrice carrée est celle dont le nombre de lignes égal au nombre de colonnes.

    Objectif:
        - Reconnaître une matrice carrée,
        - Calculer son dégré n (Nombre de lignes = Nombre de colonnes = valeur).
        - Calculer la trace notée A. (si A = aij, alors trace(A) = somme des aii pour i = 1, ...n)
'''

def calculer_trace(matrice, degre):
    trace = 0
    for i in range(degre):
        trace += matrice[i][i]
    return trace

# Exemple d'utilisation
# matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# degre = 3
# resultat = calculer_trace(matrice, degre)
# print("La trace de la matrice est :", resultat)
