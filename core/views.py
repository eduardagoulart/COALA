from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')

def sugestoes(request):
    return render(request, 'core/adotar.html')