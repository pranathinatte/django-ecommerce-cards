from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def fashion(request):
    return render(request,'fashion.html')

def grocery(request):
    return render(request,'grocery.html')

def electronics(request):
    return render(request,'electronics.html')

def healthcare(request):
    return render(request,'healthcare.html')