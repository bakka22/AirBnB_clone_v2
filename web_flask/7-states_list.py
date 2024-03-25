#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models import state, city
app = Flask(__name__)


state=state.State
@app.route('/states_list', strict_slashes=False)
def hello():
    """ print a list of states """
    global state, storage
    states = storage.all(state)
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
