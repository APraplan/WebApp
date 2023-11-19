import os
from flask import Flask, render_template, Response
import datetime

from RPi_gpio.gpio import handleRequestGPIO

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')       

@app.route('/gpio')
def gpio():
    return render_template('gpio.html')
    
@app.route('/<actionid>') 
def handleRequest(actionid):
    print("Button pressed detected in python: {}".format(actionid))
    handleRequestGPIO(actionid)
    return "OK 300"
                              
if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)