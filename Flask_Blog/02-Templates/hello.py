from flask import Flask, render_template
app = Flask(__name__)

posts = [
        {
         'author': 'Amit Vashist',
         'title' : 'Blog Post 1',
         'content': 'First Blog Post',
         'date_posted': 'Jan 07, 2019'
         },
        {
         'author': 'Amit',
         'title' : 'Blog Post 2',
         'content': 'Second Blog Post',
         'date_posted': 'Jan 08, 2019'
         }
    
    
    ]

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html', posts=posts)


@app.route("/about")
def about():
        return render_template('about.html',title='About')


if __name__ == '__main__':
        app.run(debug=True)
