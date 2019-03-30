from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    return(HttpResponse('home'))

def djangoPageView(request):
    return(render(request, "django.html"))

def affichagePageView(request):
    return(render(request, "affichage.html"))

def templatesPageView(request):
    return(render(request, "templates.html"))