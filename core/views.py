from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def sugestoes(request):
    return render(request, 'core/sugestoes.html')


def sobre(request):
    return render(request, 'core/sobre.html')


def contato(request):
    return render(request, 'core/contato.html')