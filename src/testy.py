from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/lighting')
def lighting():
    return 'Lighting control!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

