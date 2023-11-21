def transposer_matrice(matrice, degre):
    matrice_transposee = [[0 for _ in range(degre)] for _ in range(degre)]
    
    for i in range(degre):
        for j in range(degre):
            # avant
            print(matrice_transposee)
            matrice_transposee[j][i] = matrice[i][j]
            
            # après
            print(matrice_transposee)
            
    print("La matrice transposée est :")
    for ligne in matrice_transposee:
        print(ligne)
        
    return matrice_transposee

# Exemple d'utilisation
# matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# degre = 3
# matrice_transposee = transposer_matrice(matrice, degre)

