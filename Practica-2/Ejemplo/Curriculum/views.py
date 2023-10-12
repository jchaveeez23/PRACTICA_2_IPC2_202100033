from django.shortcuts import render
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/cv.html', {})
# Create your views here.
