from flask import Flask, render_template
from fn_graph import *

app = Flask(__name__)


@app.route('/')  # routing ties webpage to Python function
def index():
    result_int = distance("Lonely Lodge", (21, 91))
    return render_template("homepage.html", result_int=result_int)


if __name__ == '__main__':
    app.run()




