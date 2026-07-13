from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello<h1/>' \
    '<h2>wellcome to my first flask website</h2>'

@app.route('/about')
def about():
    return '.این صفحه ی دربارهی ماست' 

@app.route('/contact')
def contact():
    return '.برای تماس با ما به این آدرس ایمیل بزنید' 


if __name__ == '__main__':
    app.run(debug=True)