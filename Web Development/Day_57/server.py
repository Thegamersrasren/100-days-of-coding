
from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests
app = Flask(__name__)
cyear = datetime.now().year
@app.route("/")
def home():
 
    random_number = random.randint(1,20)
    return render_template("hello.html", num =random_number, copyright=cyear)
@app.route("/guess/<name>")
def gender(name):
    url =f"https://api.genderize.io?name={name}"
    gender_url = requests.get(url)
    gender_response = gender_url.json()
    gender = gender_response["gender"]
    return render_template("guess.html",persons_name= name,ggender = gender,copyright=cyear)
@app.route("/blog")
def get_blog():
    blog_url  ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    post = response.json()
    return render_template("blog.html",pref = post,copyright=cyear)
if __name__ == "__main__":
    app.run(debug=True)