#testappserver.py

import testapp
from flask import Flask
app = Flask(__name__)

@app.route('/.')
def main_page():
    return "This is the main page. Possible commands: \n \
    /alldata or /data/bus# or /gps/bus#"

@app.route('/alldata')
def _all_data():
    return testapp._get_all_data()

@app.route('/data/<busnum>')
def _specific_data(busnum):
    return testapp._get_specific_data(busnum=busnum)

@app.route('/gps/<busnum>')
def _gps_data(busnum):
    return testapp._get_Lat(busnum=busnum)

if __name__ == '__main__':
  app.run(debug=True)
