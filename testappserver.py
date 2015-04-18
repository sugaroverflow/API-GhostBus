#testappserver.py

import testapp
from flask import Flask
app = Flask(__name__)

@app.route('/')
def _alldata():
    return testapp._get_all_data()


@app.route('/')
def gps():
    return "gps"


if __name__ == '__main__':
  app.run(debug=True)
