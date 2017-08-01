# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

#
# Flask(__name__).run()

app = Flask(__name__)

@app.route('/')
def index():
    # html_file = open('C:\Users\qhaibii\Downloads\web\index.html', 'r')
    # context = html_file.read()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


