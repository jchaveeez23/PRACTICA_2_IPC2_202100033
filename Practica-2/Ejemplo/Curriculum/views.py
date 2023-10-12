from django.shortcuts import render
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/pagina.html', {})
# Create your views here.
