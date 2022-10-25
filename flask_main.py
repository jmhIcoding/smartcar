__author__ = 'adol'
from flask import Flask, request, make_response, render_template
import sys
#if sys.platform != 'win32':
import car
car.setup()

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/go_stop")
def go_stop():
    print('flask stop')
    car.stop()
    return render_template("index.html")

@app.route("/go_up")
def go_up():
    print('flask up')
    car.forward()
    return render_template("index.html")

@app.route("/go_down")
def go_down():
    print('flask down')
    car.backward()
    return render_template("index.html")

@app.route("/go_left")
def go_left():
    print('flask left')
    car.left()
    return render_template("index.html")

@app.route("/go_right")
def go_right():
    print('flask right')
    car.right()
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9020, debug=True)