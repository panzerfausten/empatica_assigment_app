from flask import Flask
from lib.UserDispatcher import UserDispatcher
from lib.Data import Data
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
@app.route("/api/users/<int:_userId>/data/sessions")
def sessions(_userId):
	_d = Data(_userId)
	return _d.getSessions()

def getData(_userId,_sessionId,_type):
	_d = Data(_userId)
	_sid = _sessionId
	return _d.getDataFromSession(_sid,_type)
@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/BVP")
def sessionBVP(_userId,_sessionId):
	return getData(_userId,_sessionId,"BVP")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/EDA")
def sessionEDA(_userId,_sessionId):
	return getData(_userId,_sessionId,"EDA")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/HR")
def sessionHR(_userId,_sessionId):
	return getData(_userId,_sessionId,"HR")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/HR_qi")
def sessionHR_qi(_userId,_sessionId):
	return getData(_userId,_sessionId,"HR_qi")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/IBI")
def sessionIBI(_userId,_sessionId):
	return getData(_userId,_sessionId,"IBI")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/TEMP")
def sessionTEMP(_userId,_sessionId):
	return getData(_userId,_sessionId,"TEMP")

@app.route("/api/users/<int:_userId>/data/sessions/<string:_sessionId>/tags")
def sessiontags(_userId,_sessionId):
	return getData(_userId,_sessionId,"tags")

if __name__ == '__main__':
    app.run(debug=True)
