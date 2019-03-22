from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)
name = 'Skey'
movies = [
    {'title':'My Neighbor Totoro', 'year':'1988'},
    {'title':'Dead Poets Society', 'year':'1989'},
    {'title':'A Perfect World', 'year':'1993'},
    {'title':'Leon', 'year':'1994'},
    {'title':'Mahjong', 'year':'1996'},
    {'title':'Smallowtail Butterfly', 'year':'1996'},
    {'title':'King of Comedy', 'year':'1999'},
    {'title':'Devils on the Doorstep', 'year':'1999'},
    {'title':'WALL-E', 'year':'2008'},
]

@app.route('/') # Similar to the Django view
def index():
    # return  '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
    return render_template('index.html', name=name, movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return "User: %s" % name

@app.route('/test')
def test_url_for():
    print(url_for('hello')) # /
    print(url_for('user_page', name='skey')) # user_page/skey
    print(url_for('test_url_for')) # /test
    print(url_for('test_url_for', num=2))   # /test?num=2
    return 'Test Page'

if __name__ == '__main__':
    app.run()