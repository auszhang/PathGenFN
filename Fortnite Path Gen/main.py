from flask import Flask, render_template, request
from fn_graph import *

app = Flask(__name__)


@app.route('/')  # routing ties webpage to Python function
def index():
    return render_template("homepage.html")


# Two text boxes, 1 for start and the other for end
# Some kind of type checking

@app.route('/', methods=['POST'])
def magic():
    start = request.form['start']
    if start == "Unnamed Locataion":
        unnamed = request.form['unnamed']
        start = unnamed
    circle00 = request.form['circle00']
    circle01 = request.form['circle01']
    circle10 = request.form['circle10']
    circle11 = request.form['circle11']
    coordinate = circle00 + "-" + circle01 + ", " + circle10 + "-" + circle11
    processed = process_text(start, coordinate)
    add_user_input(processed)
    depth_first_search()
    path_list = format_path(gen_path())
    return render_template("homepage.html", path=path_list)
#
# @app.route('/', methods=['GET'])
# def dropdown():
#     POIs = POI_dict
#     return render_template('homepage.html', POIs=POIs)

if __name__ == '__main__':
    app.debug = True
    app.run()





