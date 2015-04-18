
from flask import Flask
app = Flask(__name__)

@app.route('/')
    def mainFunc():
        return "hello test"


@app.route('/getBusNum')
def hello_world():
    return "hi"

@app.route('/getGPS')
def gps():
    return "gps"




if __name__ == '__main__':
    app.run(debug=True)
