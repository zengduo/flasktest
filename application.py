from flask import Flask, render_template
# from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

# manager = Manager(app)
bootstrap = Bootstrap(app)

DEBUG = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
