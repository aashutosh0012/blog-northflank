from django.shortcuts import render

# def consulting_home(request):
#     return render(request,'templates/consulting_home.html')

def home(request):
    return render(request,'templates/consulting_home.html')

def portfolio(request):
    return render(request,'templates/portfolio.html')

def jira(request):
    return render(request,'templates/consulting/jira.html')

def contact_us(request):
    return render(request,'templates/contact_us.html')