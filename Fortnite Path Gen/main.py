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
    text1 = request.form['text1']
    processed = process_text(start, text1)
    add_user_input(processed)
    depth_first_search()
    path_list = gen_path()
    return format_path(path_list)
#
# @app.route('/', methods=['GET'])
# def dropdown():
#     POIs = POI_dict
#     return render_template('homepage.html', POIs=POIs)

if __name__ == '__main__':
    app.debug = True
    app.run()




