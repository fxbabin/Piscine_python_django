from django.shortcuts import render, HttpResponse
from ex02.forms import MyForm
import os.path
import datetime
from django.conf import settings
# Create your views here.

def getHistory():
    history = []
    if not os.path.isfile(settings.HISTORY_FILE):
        return ([])
    with open(settings.HISTORY_FILE, 'r') as in_file:
        for line in in_file:
            history.append(line)
    return (history)

def formPageView(request):
    history = getHistory()
    if (request.method == "POST"):
        form = MyForm(request.POST)
        if form.is_valid():
            message_date = "{} {}".format(form.cleaned_data['message'] ,datetime.datetime.now())
            with open(settings.HISTORY_FILE, 'a') as hist_file:
                hist_file.write("{}\n".format(message_date))
            history.append(message_date)
    else:
        form = MyForm()
    return(render(request, "form.html", {'form': form, 'history': history}))