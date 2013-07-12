from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/post")
def post():
	
    post = model.get_post()
    return render_template("index.html", title = post.title,
										user_id = post.user_id,
										body = post.body,
                                        created_at = post.created_at)

if __name__=="__main__":
	app.run(debug=True)