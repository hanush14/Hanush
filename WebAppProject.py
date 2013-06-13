import os
import pyramid.chameleon_text
import pyramid.session

from views import myview


def make_text(string):
    return string

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
    web.form.Textbox('', class_='emailid', id='emailid'),
    )

class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Enter your email id here")

config.add_route('myroute','/prefix/(one)/{two}')
config.scan('emailid')

#Database Call
import MySQLdb

user = User.objects.create_user("emailid")

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="14081408",
                     db="database")

cur = db.cursor()
table_name = "userinformation"

countUserId = cur.execute ("SELECT count(*) from userinformation where Useremailid='emailid'")
    nlines = cur.execute ("INSERT INTO userinformation VALUES ('emailid')")
    db.commit()

config.add_route('myroute','/prefix/(one)/{two}')
else:
    print "Page 2"

for row in cur.fetchall() :
    print row[0]


#Hello_World

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def hello_json(request):
    return request.matchdict

if __name__ == '__main__':

    config = Configurator()
    config.add_route(name='hello', pattern='/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    config.add_route(name='hello_json', pattern='/json/{name}')
    config.add_view(hello_json, route_name='hello_json', renderer='json')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Server started at http://localhost:8080")
    server.serve_forever()


#AJAX Call
import web

def make_text(string):
    return string

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
    web.form.Textbox('', class_='post', id='post'),
    )

class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Your text goes here.")

    def POST(self):
        form = my_form()
        form.validates()
        s = form.value['post']
        return make_text(s)

if __name__ == '__main__':
    app.run()


#DatabaseCall

user = User.objects.create_user("post","time","day")

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="14081408",
                     db="database")

cur = db.cursor()
table_name = "userinformation"

countUserId = cur.execute ("SELECT count(*) from userinformation where Useremailid='post','time','day'")

for row in cur.fetchall() :
    print row[0]


#Column Call

import MySQLdb
from pyramid.chameleon_text import __call__

for user = User.objects.create_user("emailid")

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="14081408",
                     db="database")

cur = db.cursor()
table_name = "userinformation"

countUserId = cur.execute ("SELECT count(*) from userinformation where Useremailid='emailid'")
    print "'emailid' said 'post' at 'time' on 'day'"

for row in cur.fetchall() :
    print row[0]
