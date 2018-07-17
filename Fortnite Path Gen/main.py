from flask import Flask, render_template, request
from fn_graph import *

app = Flask(__name__)


@app.route('/')  # routing ties webpage to Python function
def index():
    # result_int = distance("Lonely Lodge", (21, 91))
    return render_template("homepage.html")  # , result_int=result_int)

# Two text boxes, 1 for start and the other for end
# Some kind of type checking

# @app.route('/', methods='POST')
# def index():
#     coords = request.form['text']
#     processed_text = text.upper();


if __name__ == '__main__':
    app.run()




