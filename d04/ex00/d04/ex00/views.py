from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Welcome!')

def testPageView(request):
    return render(request, "ex00/index.html")