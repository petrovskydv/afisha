from django.shortcuts import render


def index(request):
    print("новое приложение")
    return render(request, 'index.html')
