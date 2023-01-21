from flask import Flask, render_template, url_for
from faux.data import posts

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/blog/')
def blog_feed():
	return render_template('blogfeed.html', posts=posts)


@app.route('/blog/<slug>')
def blog_post(slug):
	post = [post for post in posts if post["slug"] == slug][0]
	return render_template('blogpost.html', post=post)


@app.route('/contact/')
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run()
