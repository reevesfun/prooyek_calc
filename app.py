from flask import Flask, render_template, request

from bata import bata
from pasir import pasir
from semen import semen
from platBaja import platBaja

import math
import locale

#Declare
app = Flask(__name__)

app.register_blueprint(bata, url_prefix="")
app.register_blueprint(semen, url_prefix="")
app.register_blueprint(pasir, url_prefix="")
app.register_blueprint(platBaja, url_prefix="")

# Start an app route ('/')
@app.route('/')
def main():
    return render_template('index.html')