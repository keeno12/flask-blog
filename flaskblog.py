from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Keenan Olsen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 28, 2019'
    },
    {
        'author': 'George Washington',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 28, 2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return '<h1>I made an about page!!</h1>'
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)    