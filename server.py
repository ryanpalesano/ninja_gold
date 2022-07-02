from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="I am secret"

import random



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    if "activities" not in session:
        session["activities"] = []
    else:
        session["activities"] = session["activities"]
    if "gold" not in session:
        session["gold"] = 0
    if request.form["building"] == "farm":
        earn = random.randint(10,20)
        session["gold"] += earn
        session["activities"].append(f"<div class='text-success'>Earned {earn} from the farm</div>")
    elif request.form["building"] == "cave":
        earn = random.randint(5,10)
        print(earn)
        session["gold"] += earn
        session["activities"].append(f"<div class='text-success'>Earned {earn} from the cave</div>")
    elif request.form["building"] == "house":
        earn = random.randint(2,5)
        session["gold"] += earn
        session["activities"].append(f"<div class='text-success'>Earned {earn} from the earn</div>")
    elif request.form["building"] == "casino":
        earn = random.randint(-50,50)
        session["gold"] += earn
        if earn > 0:
            session["activities"].append(f"<div class='text-success'>Earned {earn} from the casino</div>")
        else:
            session["activities"].append(f"<div class='text-danger'>Earned {earn} from the casino</div>")

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5003)


