from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306207013',
        'name'  : 'Micheline Wijaya Limbergh',
        'class' : 'PBP D',
    }

    return render(request, 'main.html', context)
