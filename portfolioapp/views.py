from django.shortcuts import render

# Create your views here.
############# HOME VIEW ################

def Home(request):
    return render(request,'portfolioapp/home.html')
