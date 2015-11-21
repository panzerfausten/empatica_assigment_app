import os
import json
from Session import Session
class DeviceStatus:
	def __init__(self,device):
		self.device = device
		self._dataFolder = "data/" #TODO: Fix this
		self.findSessions()
	def findSessions(self):
		self._sessions = []
                for _folder in reversed(os.listdir(self._dataFolder)):
			if self.device in _folder: #get sessions only from the specified device
				_file = self._dataFolder + _folder
				self._sessions.append(_file)
	def doTests(self,_json=True):
		#create a new session and call check to the last 5 sessions
		_results = []
		_resultJson = {"device_id":self.device,"tests":[]}
		for _x,_s in  enumerate(self._sessions):
			_se = Session(_s)
			_res = _se.checkSessionStatus()
			_results.append(_res)
			_resultJson["tests"].append(_res)
			if _x == 4:
				break
		if(_json):
			return json.dumps(_resultJson)
		else:
			return _results
