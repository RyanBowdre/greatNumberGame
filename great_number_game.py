from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'jkhkjhkjhkj'
import random

@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def number_pick():
    session['new_string'] = ""
    session['user_number'] = int(request.form['text'])
    if session['user_number'] > session['random_num']:
        session['new_string'] = "TOO HIGH!"
    elif session['user_number'] < session['random_num']:
        session['new_string'] = "TOO LOW!"
    elif session['user_number'] == session['random_num']:
        session['new_string'] = "YOU WIN! The number was " + str(session['random_num'])
    else:
        return redirect ("/")

    print session['random_num']
    print session['user_number']
    print session['new_string']
    return redirect ("/")


@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect ("/")



app.run(debug=True)
