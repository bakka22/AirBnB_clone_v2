#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello():
    """ print a list of states """
    global storage
    states = storage.all("State")
    state_list = []
    for k, state in states.items():
        state_list.append(state)
    state_list.sort(key=lambda x: x.name)
    return render_template("7-states_list.html", state_list=state_list)


@app.teardown_appcontext
def reset(exception):
    storage.close()


if __name__ == ('__main__'):
    app.run()
