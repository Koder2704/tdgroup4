from django.shortcuts import render
from .models import Exercice, Author

# Import @Daniel:
from .utils.exo17 import calculer_schtroumpf
from .utils.exo22 import calculer_trace
from .utils.exo23 import transposer_matrice
# Fin import @Daniel


# ============================================================ @DANIEL ==================================================================
HTML_FILE_NAME = 'details.html'
def to_str(input: str):
    try:
        return int(input)
    except ValueError:
        try: 
            return float(input)
        except ValueError:
            return input
        
def to_matrix(data: str) -> list:
    elements = data.strip('[]').replace(' ', '').split(',')
    elements = [to_str(e) for e in elements]
    taille = len(elements)
    matrix = [elements[i:i+len(elements)] for i in range(0, len(elements), taille)]
    return matrix


def index(request):
    exercices_list = Exercice.objects.order_by('-created_at')
    context = { 'exercices_list': exercices_list}

    return render(request, 'index.html', context)


def show_more_for_daniel(request, pk):
    exercice = Exercice.objects.get(id=pk)
    
    '''
    Variables placeholder1 et placeholder2, qui seront dynamique afin de changer
    selon le genre d'entrée attendue par l'application.
    '''
    placeholder1 = '',
    placeholder2 = ''
    
    # Message d'erreur à afficher:
    error_message = ''
    
    # les tableaux qui contiendront les résultats.
    # Uniquement pour exercice 17:
    tab1 = []
    tab2 = []
    
    # Uniquement pour exercice 22 et 23:
    matrice = []
    degre_matrice = 0
    
    
    # Les variables qui vont garder les entrées des utilisateurs:
    first_input, second_input = request.POST.get('first_input'), request.POST.get('second_input')
    
    # 
    if exercice.title == 'Les Schtroumpfs':
        placeholder1 = 'Entrez le premier tableau: (ex: [a, b, c, ...])'
        placeholder2 = 'Entrez le deuxième tableau: (ex: [d, e, f, ...])'
        
        if first_input != None or second_input != None: 
            # J'essaye un bloc...
            try:
                
                # Cas où tout marche bien, fait ceci 👇
                tab1, tab2 = first_input.strip('[]').replace(' ', ''), second_input.strip('[]').replace(' ', '')
                tab1, tab2 = tab1.split(','), tab2.split(',')
                
                tab1, tab2 = [int(fi) for fi in tab1], [int(si) for si in tab2]
                print('Converted first:', tab1)
                print('Converted second:', tab2)
                
                # Calcul de la valeur des schtroumpfs:
                if len(tab1) == len(tab2):
                    exercice.resultat = calculer_schtroumpf(tab1, tab2)
                    print(exercice.resultat)
                else:
                    error_message = "Les tableaux doivent avoir la même taille."
                

                # S'il arrive une erreur de type 'ValueError' (Erreur dans la valeur entrée)...
            except:
                # Fais ceci: 👇
                error_message = 'Les valeurs des tableaux entrés ne sont pas valides.'
                
        else: 
            print('No given values')
            error_message = "Aucun champ ne doit être vide !"
    elif pk == 2:
        placeholder1 = 'Entrez la matrice: (ex: [[a, b, c], [d, e, f], ..., [g, h, i]])'
        placeholder2 = 'Entrez le dégré de cette matrice'
        
        if first_input != None or second_input != None: 
            matrice = to_matrix(first_input)
            print("Matrice:", matrice)
        else: 
            error_message = "Aucun champ ne doit être vide !"
            
            
    context = { 
        'exercice': exercice,
        'placeholder1': placeholder1,
        'placeholder2': placeholder2,
        'error_message': error_message
    }
    

    return render(request, HTML_FILE_NAME, context)

# ================================================================= FIN @DANIEL =============================================================
 
 
 
 # ============================================================ @REX ==================================================================
def show_more_for_rex(request, pk):
    print('Page ID:', pk)
    return render(request, HTML_FILE_NAME)
# ================================================================= FIN @REX =============================================================

 
 # ============================================================ @SAMANTHA ==================================================================
def show_more_for_samantha(request, pk):
    print('Page ID:', pk)
    return render(request, HTML_FILE_NAME)
# ================================================================= FIN @SAMANTHA =============================================================
