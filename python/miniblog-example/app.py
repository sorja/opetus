from flask import Flask, render_template, session, redirect, url_for, escape, request
from time import ctime

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile')
def profile():
    posts = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent et felis a nulla lobortis malesuada a ut lorem. ".split( )
    return render_template("profile.html", posts=posts)

if __name__ == "__main__":
    app.run()
