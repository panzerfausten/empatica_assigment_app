from flask import Flask
from flask import render_template
from lib.UserDispatcher import UserDispatcher
from lib.Data import Data
from lib.Session import Session
from lib.DeviceStatus import DeviceStatus
app = Flask(__name__)
@app.route("/api/users/<int:_userId>")
def users(_userId):
	u = UserDispatcher()
	return u.get(_userId)
@app.route("/api/users/<int:_userId>/devices")
def devices(_userId):
	u = UserDispatcher()
	return u.getDevices(_userId)

@app.route("/api/device/<string:_deviceId>/")
def support_api(_deviceId):
	_ds = DeviceStatus(_deviceId)
	_resTests = _ds.doTests()	
	return _resTests
@app.route("/api/users/<int:_userId>/data")
def data(_userId):
	return "OK"

@app.route("/api/users/<int:_userId>/data/sessions/")
def sessions(_userId):
	_d = Data(_userId)
	return _d.getSessions()

def getData(_userId,_sessionId,_type,_json=True):
	_d = Data(_userId)
	_sid = _sessionId
	return _d.getDataFromSession(_sid,_type,_json)
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
##app###
@app.route("/")
def login():
	return render_template("login.html")
@app.route("/app/user/<int:_userId>/sessions")
def userSessions(_userId):
	_d = Data(_userId)
	_sessions = _d.getSessions(False)
	u = UserDispatcher()
	_user = u.get(_userId,False)
	return render_template("userFeed.html",user = _user,sessions = _sessions)
@app.route("/app/user/<int:_userId>/sessions/<string:_sessionId>")
def userSession(_userId,_sessionId):
	u = UserDispatcher()
	_user = u.get(_userId,False)
	_d = Data(_userId)
	_sessionEDA = getData(_userId,_sessionId,"EDA",_json=False)
	try:
		_sessionHR = getData(_userId,_sessionId,"HR",_json=False)
		_sHR = _sessionHR["session"]["data"]["HR"]
	except:
		_sHR = []
	try:
		_sessionTEMP = getData(_userId,_sessionId,"TEMP",_json=False)
		_sTEMP =  _sessionTEMP["session"]["data"]["TEMP"]
	except:
		_sTEMP = []
	_sEDA =  _sessionEDA["session"]["data"]["EDA"]
	return render_template("sessionData.html",user = _user,_sessionHR = _sHR,_sessionEDA = _sEDA,_sessionTEMP = _sTEMP,_metadata = _sessionEDA["session"]["metadata"])
@app.route("/app/support")
def support():
	return render_template("support.html")

@app.route("/app/support/<string:deviceId>")
def support_device(deviceId):
	_ds = DeviceStatus(deviceId)
	_resTests = _ds.doTests(False)
	return render_template("support_results.html",_resTests = _resTests,_device= deviceId)
if __name__ == '__main__':
    app.run(debug=True)
