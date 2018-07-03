from flask import Flask, render_template
from fn_graph import *

app = Flask(__name__)


@app.route('/') # routing ties webpage to Python function
def index():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()

