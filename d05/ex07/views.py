from django.shortcuts import render, HttpResponse
from .models import Movies

# Create your views here.
def populate(request):
    try:

        out = ""
        movie = "The Phantom Menace"
        m = Movies(
            episode_nb='1',
			title = 'The Phantom Menace', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '1999-05-19'
        )
        m.save()
        out += "OK<br>"
        
        movie = "Attack of the Clones"
        m = Movies(
            episode_nb='2',
			title = 'Attack of the Clones', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '2002-05-16'
        )
        m.save()
        out += "OK<br>"

        movie = "Revenge of the Sith"
        m = Movies(
            episode_nb='3',
			title = 'Revenge of the Sith', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '2005-05-19'
        )
        m.save()
        out += "OK<br>"

        movie = "A New Hope"
        m = Movies(
            episode_nb='4',
			title = 'A New Hope', 
			director = 'George Lucas', 
			producer = 'Gary Kurtz, Rick McCallum', 
			release_date = '1977-05-25'
        )
        m.save()
        out += "OK<br>"

        movie = "The Empire Strikes Back"
        m = Movies(
            episode_nb='5',
			title = 'The Empire Strikes Back', 
			director = 'Irvin Kershner', 
			producer = 'Gary Kutz, Rick McCallum', 
			release_date = '1980-05-17'
        )
        m.save()
        out += "OK<br>"
        
        movie = "Return of the Jedi"
        m = Movies(
            episode_nb='6',
			title = 'Return of the Jedi', 
			director = 'Richard Marquand', 
			producer = 'Howard G. Kazanjian, George Lucas, Rick McCallum', 
			release_date = '1983-05-25'
        )
        m.save()
        out += "OK<br>"
        
        movie = "The Force Awakens"
        m = Movies(
            episode_nb='7',
			title = 'The Force Awakens', 
			director = 'J. J. Abrams', 
			producer = 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 
			release_date = '2015-12-11'
        )
        m.save()
        out += "OK<br>"

        return HttpResponse(out)
    except Exception as e:
        return HttpResponse("{} ::: {}".format(movie, e))
    return HttpResponse('you should not be here!')

def delete(request):
    try:
        r = Movies.objects.all()
        r.delete()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')


def display(request):
    try:
        r = Movies.objects.all()

        if not r:
            return HttpResponse('No data available')
        res = "<table style='border: 1px solid black; border-collapse: collapse;'>"
        for m in r:
            res += '<tr style="border: 1px solid black;">'
            res += """
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            <td style='border: 1px solid black;'> {} </td>
            """.format(m.episode_nb, m.title, m.opening_crawl, m.director, m.producer, m.release_date, m.created, m.updated)
        res += "</table>"
        return HttpResponse(res)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')

def update(request):
    try:
        r = Movies.objects.all()

        if not r:
            return HttpResponse('No data available')
        
        movies = []
        for m in r:
            movies.append(m.title)
        if request.method == 'POST' :
            title = request.POST['type']
            crawl = request.POST['crawl']
            if title:
                Movies.objects.filter(title = title).update(opening_crawl=crawl)
                res = Movies.objects.filter(title = title)
                if not res:
                    return HttpResponse('No data available')
        return render(request, 'update.html', {'movies': movies})
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')

