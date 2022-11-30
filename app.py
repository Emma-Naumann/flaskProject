from flask import Flask

# create an instance of Flask class called ap
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def f(celsius: str):
    return f"{celsius} degrees Celsius is equivalent to {str(float(celsius) * 9.0 / 5 + 32)} degrees Fahrenheit."


if __name__ == '__main__':
    app.run()
