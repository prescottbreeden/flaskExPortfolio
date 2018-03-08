from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('index.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/about_me')
def about():
	return render_template('about_me.html')

app.run(debug=True)