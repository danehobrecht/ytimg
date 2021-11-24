#!/venv/bin/python3

from flask import Flask, request, redirect, render_template
from main import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		i = request.form['url']
		o = main(i)
		return redirect(o)
	return render_template('home.html')
