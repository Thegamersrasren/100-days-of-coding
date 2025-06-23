from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye!</p>"
@app.route("/username/<name>/<int:number>")
def greet(nam,number):
    return f"<p>hello {nam}, you are {number} years old<p>"
if __name__ == "__main__":
    app.run(debug = True)

