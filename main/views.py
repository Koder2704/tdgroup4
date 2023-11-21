from django.shortcuts import render
from .models import Exercice, Author
from .utils.exo17 import calculer_schtroumpf
from .utils.exo22 import calculer_trace
from .utils.exo23 import transposer_matrice

# Create your views here.
def index(request):
    exercices_list = Exercice.objects.order_by('-created_at')
    context = { 'exercices_list': exercices_list}

    return render(request, 'index.html', context)


def show_more(request, pk):
    exercice = Exercice.objects.get(id=pk)
    placeholder1 = '',
    placeholder2 = ''
    tab1 = []
    tab2 = []
    
    first_input, second_input = request.POST.get('first_input'), request.POST.get('second_input')
    
    if exercice.title == 'Les Schtroumpfs':
        placeholder1 = 'Entrez le premier tableau: (ex: [a, b, c, ...])'
        placeholder2 = 'Entrez le deuxième tableau: (ex: [d, e, f, ...])'
        
        if first_input != None or second_input != None: 
            tab1, tab2 = first_input.strip('[]').replace(' ', ''), second_input.strip('[]').replace(' ', '')
            tab1, tab2 = tab1.split(','), tab2.split(',')
            
            tab1, tab2 = [int(fi) for fi in tab1], [int(si) for si in tab2]
            print('Converted first:', tab1)
            print('Converted second:', tab2)
            
            # Calcul de la valeur des schtroumpfs:
            exercice.resultat = calculer_schtroumpf(tab1, tab2)
            print(exercice.resultat)
        else: 
            print('No given values')
    else:
        placeholder1 = 'Entrez la matrice: (ex: [[a, b, c], [d, e, f], ..., [g, h, i]])'
        placeholder2 = 'Entrez le dégré de cette matrice'
    
    

    context = { 
               'exercice': exercice,
               'placeholder1': placeholder1,
               'placeholder2': placeholder2
               }

    

    return render(request, 'details.html', context)
 