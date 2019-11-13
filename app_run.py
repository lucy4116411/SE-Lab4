
from flask import *
from datetime import datetime
import SimpleCalculator as cal
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return render_template('index.html')

@app.route('/add')
def add():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(cal.add(a,b))

@app.route('/minus')
def minus():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(cal.minus(a,b))

@app.route('/multi')
def times():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(cal.multi(a,b))

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    app.run(debug=True)
