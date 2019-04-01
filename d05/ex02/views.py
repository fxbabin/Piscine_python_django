from django.shortcuts import render, HttpResponse
import psycopg2

# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )    

        curr = conn.cursor()

        curr.execute(""" 
        CREATE TABLE IF NOT EXISTS ex02_movies (
            title           varchar(64)     NOT NULL UNIQUE,
            episode_nb      integer         PRIMARY KEY,
            opening_crawl   text,
            director        varchar(32)     NOT NULL,
            producer        varchar(128)    NOT NULL,
            release_date    date            NOT NULL
        )
        """)
        conn.commit()
        conn.close()
        return HttpResponse('OK')
    except psycopg2.Error as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')

def populate_insert(curr, query, title):
    try:
        curr.execute(query)
        curr.commit()
        return ("OK<br>")
    except psycopg2.Error as e:
        print("{} : {}\n".format(title, e))
        return("")

def populate(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )    

        curr = conn.cursor()

        out = ""
        movie = "The Phantom Menace"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('1',
                 'The Phantom Menace',
                 'Georges Lucas',
                 'Rick McCallum',
                 '1999-05-19')
        """)
        out += "OK<br>"

        movie = "Attack of the Clones"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('2',
                 'Attack of the Clones',
                 'Georges Lucas',
                 'Rick McCallum',
                 '2002-05-16')
        """)
        out += "OK<br>"

        movie = "Revenge of the Sith"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('3',
                'Revenge of the Sith',
                'Georges Lucas',
                'Rick McCallum',
                '2005-05-19')
        """)
        out += "OK<br>"

        movie = "A New Hope"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('4',
                 'A New Hope',
                 'Georges Lucas',
                 'Gary Kurtz, Rick McCallum',
                 '1977-05-25')
        """)
        out += "OK<br>"

        movie = "The Empire Strikes Back"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('5',
                 'The Empire Strikes Back',
                 'Irvin Kershner',
                 'Gary Kutz, Rick McCallum',
                 '1980-05-17')
        """)
        out += "OK<br>"

        movie = "Return of the Jedi"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('6',
                 'Return of the Jedi',
                 'Richard Marquand',
                 'Howard G. Kazanjian, George Lucas, Rick McCallum',
                 '1983-05-25')
        """)
        out += "OK<br>"

        movie = "The Force Awakens"
        curr.execute(""" 
        INSERT INTO ex02_movies
                (episode_nb, title, director, producer, release_date)
        VALUES  ('7',
                 'The Force Awakens',
                 'J. J. Abrams',
                 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
                 '2015-12-11')
        """)
        out += "OK<br>"

        conn.commit()
        conn.close()
        return HttpResponse(out)
    except psycopg2.Error as e:
        return HttpResponse("{} ::: {}".format(movie, e))
    return HttpResponse('you should not be here!')

def display(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )    

        curr = conn.cursor()

        curr.execute("SELECT * FROM ex02_movies")
        response = curr.fetchall()
		
        if not response:
            return HttpResponse('No data available')
        res = "<table style='border: 1px solid black; border-collapse: collapse;'>"
        for r in response:
            res += '<tr style="border: 1px solid black;">'
            for e in r:
                res += "<td style='border: 1px solid black;'>" + str(e) + "</td>"
        res += "</table>"
        conn.commit()
        conn.close()
        return HttpResponse(res)
    except psycopg2.Error as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')


def delete(request):
    try:
        conn = psycopg2.connect(
            database = 'formationdjango',
            host = 'localhost',
            user = 'djangouser',
            password = 'secret'
        )
        curr = conn.cursor()
        curr.execute("DELETE FROM ex02_movies")
        conn.commit()
        conn.close()
        return HttpResponse('OK')
    except psycopg2.Error as e:
        return HttpResponse(e)
    return HttpResponse('you should not be here!')