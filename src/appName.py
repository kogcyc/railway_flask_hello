import flask
import os

app = flask.Flask(__name__)

ss = os.getenv('SUPER_SECRET')

@app.route('/')
def index():
    return f'Hello World!, my secret is {ss}'

if __name__ == '__main__':
    app.run()
