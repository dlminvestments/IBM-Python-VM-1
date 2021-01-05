pip install -U Flask

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
$ env FLASK_APP=hello.py flask run
 * Serving Flask app "hello"
 * Running on http://100.2.194.152/32 /
