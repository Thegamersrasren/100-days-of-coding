from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Best anime.html")
if __name__ == "__main__":
    app.run()