import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "I am a key"

@app.route('/')
def index():
    if 'total' in session:
        total = session['total']
    else:
        session['total'] = 0
    return render_template("index.html", count = total) #count = 3

@app.route('/process_money', methods=['POST'])
def process():

    print(request.form['building'])

    if request.form['building'] == 'farm':
        session['total'] += random.randrange(10,20)
    elif request.form['building'] == 'cave':
        session['total'] += random.randrange(5,10)
    elif request.form['building'] == 'house':
        session['total'] += random.randrange(2,5)
    elif request.form['building'] == 'casino':
        session['total'] += random.randrange(0,50)

    print(session['total'])

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)



