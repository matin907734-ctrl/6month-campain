from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'یک-رشته-تصادفی-و-مخفی'
topics = ['Html', 'css', 'javascript', 'python']

@app.route('/')
def home():
    return render_template('index.html', name='matin', age='15')

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
            flash('you forgot the name')
            return redirect(url_for('register'))
        if not age:
            flash('you forgot the age')
            return redirect(url_for('register'))
        flash(f'welcome {username}!you succsed')
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

@app.route('/subjects')
def subjects():
    return render_template('subjects.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)