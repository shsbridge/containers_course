from flask import Flask, render_template, request, flash
import random

application = Flask(__name__)
application.secret_key = "asdfasdfasdfasdfasdf"

@application.route("/",methods=['GET'])
def index():
	flash( "message" + str(random.randrange(1,6,1)) )
	return render_template("index.html")

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()