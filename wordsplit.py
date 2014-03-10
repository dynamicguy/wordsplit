import os
from flask import Flask
from ngrams import *

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def wordsplit(path):
    return 'Your splitted sentence is: %s' % ' '.join(segment(path))