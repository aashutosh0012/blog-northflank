from django.shortcuts import render

def home(request):
    return render(request,'templates/home.html')

def portfolio(request):
    return render(request,'templates/portfolio.html')