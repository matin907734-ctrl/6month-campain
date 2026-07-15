from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='matin', age='15')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return '.برای تماس با ما به این آدرس ایمیل بزنید' 

@app.route("/me")
def me():
    return "i'm Matin"

@app.route('/subjects')
def subjects():
    topics = ['Html', 'css', 'javascript', 'python']
    return render_template('subjects.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)