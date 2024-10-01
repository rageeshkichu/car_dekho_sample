from django.shortcuts import render

def HomePage(request):
    return render(request,'HomePage.html')

def loginorsignup(request):
    return render(request,'Login.html')
