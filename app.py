from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='My Calculator')

@app.route('/LoanPayment', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        form = request.form
        A = float(form['A'])
        n = float(form['n']) * 12
        i = float(form['i']) / 12
        dscnt = ( ( (1 + i) **n) - 1) / (i * (1 + i) **n)
        borrowed = A/dscnt
        return render_template('index.html', display=borrowed, pageTitle='My Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)

