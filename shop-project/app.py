from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'یک-رشته-تصادفی-و-مخفی'
topics = ['Html', 'css', 'javascript', 'python']
# products = ['book', 'mouse', 'headphone', 'pc']

db = SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.title}>'

@app.route('/')
def home():
    session['visits'] = session.get('visits', 0) + 1
    return render_template('index.html', name='matin', age='15', visits=session['visits'] )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return '.برای تماس با ما به این آدرس ایمیل بزنید' 

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')
        if not username:
            return render_template('register.html', error="you forgot the name ")
        if not age:
            return render_template('register.html', error="you forgot the age " )
        flash(f'welcome {username} register succesfull')
        return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/search', methods=['GET','POST'])
def search():
    query = request.args.get('q', '')
    results = []
    if query:
        results = [item for item in topics if query.lower() in item.lower()]
        if results:
            flash(f'found {len(results)} results for {query}')
        else:
            flash(f'No results found for {query}')
    return render_template('search.html', query=query, results=results)

@app.route('/add/<item>')
def add_to_cart(item):
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return f'{item} append to the list. list now {cart}'

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', items=cart)

@app.route('/shop-list')
def shop_list():
    cart = session.get('cart', [])
    return render_template('shop_list.html', items=cart)

@app.route('/clear-cart')
def clear_cart():
    session.pop('cart', None)
    return '<h1>deleted shop List'

@app.route('/set-theme/<theme>')
def set_theme(theme):
    response = make_response(f'change theme to {theme}')
    response.set_cookie('theme', theme, max_age=60*60*24*30)
    return response

@app.route('/show_theme')
def show_theme():
    theme = request.cookies.get('theme', 'light')
    return f'you theme:{theme}'

@app.route('/subjects')
def subjects():
    return render_template('subjects.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)