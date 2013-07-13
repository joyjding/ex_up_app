from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)

@app.route("/") # display all posts on the index page
def index():
	model.connect_to_db() # connect to database, using code from model
	# do I need the post id?
	# what exactly is happening here?
	posts = model.get_all_posts()

	return render_template("index.html", all_posts = posts)

if __name__=="__main__":
	app.run(debug=True)