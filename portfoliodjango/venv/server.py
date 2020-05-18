from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/templates/works.html')
def work():
    return render_template('works.html')

@app.route('/about')
def hello_wor():
    return render_template('about.html')

