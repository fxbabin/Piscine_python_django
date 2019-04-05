from django.shortcuts import render
from .forms import FileForm
from .models import File

# Create your views here.

def home(request):
    files = File.objects.all()
    #File.objects.all().delete()
    #for f in files:
    #    print(f.name, f.file.url)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileForm()
    return render(request, 'ex00/home.html', {'form': form, 'files': files})