from flask import Flask
from lib.UserDispatcher import UserDispatcher
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World!'
@app.route("/api/users/<int:_userId>")
def users(_userId):
	u = UserDispatcher()
	return u.get(_userId)
@app.route("/api/users/<int:_userId>/devices")
def devices(_userId):
	u = UserDispatcher()
	return u.getDevices(_userId)
@app.route("/api/users/<int:_userId>/data")
def data(_userId):
	return "OK"

if __name__ == '__main__':
    app.run(debug=True)
