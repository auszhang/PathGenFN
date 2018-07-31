from flask import Flask, render_template, request
from fn_graph import *

app = Flask(__name__)


@app.route('/')  # routing ties webpage to Python function
def index():
    return render_template("homepage.html")


# Two text boxes, 1 for start and the other for end
# Some kind of type checking

@app.route('/', methods=["POST"])
def index_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    processed = process_text(text1, text2)
    add_user_input(processed)
    # gen_edges()
    depth_first_search()
    path_list = gen_path()
    return format_path(path_list)


if __name__ == '__main__':
    app.debug = True
    app.run()




