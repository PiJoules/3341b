# Call vendor to add the dependencies to the classpath
import vendor
vendor.add('lib')


# Import the Flask Framework
from flask import Flask, render_template, url_for, current_app
app = Flask(__name__)


import json


# Root directory
@app.route('/')
def index():
	with current_app.open_resource("people.json") as f:
		people = json.load(f)
	with current_app.open_resource("projects.json") as f:
		projects = json.load(f)
	return render_template("index.html", people=people, projects=projects)


if __name__ == '__main__':
    app.run()

