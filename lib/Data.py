from UserDispatcher import UserDispatcher
from Session import Session
import os
import json 
class Data:
	def __init__(self,userId):
		_userDispatcher = UserDispatcher()
		self._dataFolder = "data/"
		self.userId = userId
		self.user = _userDispatcher.get(userId,False)
		self.devices = self.user.devices
	def getSessions(self,_json=True):
		_availableSessions = {"sessions":[],"count":0}
		_nSessions = 0 
		for _folder in reversed(os.listdir(self._dataFolder)):
			for _device in self.devices:
				if _device in _folder: #get only the folders from his/her device
					_file = self._dataFolder + _folder 
					_d = Session(_file)
					_availableSessions["sessions"].append(_d.getMetaDataOnly())
					_nSessions += 1
		_availableSessions["count"] = _nSessions

		if(_json):
			return json.dumps(_availableSessions)
		else:
			return _availableSessions
	def getSupportSession(self,session):
		pass	

	def getDataFromSession(self,session,signalType,_json=True):
		_file = self._dataFolder +session
		_d = Session(_file)
		return _d.getData(signalType,_json)
	def getDataByDate(self,session,signals):
		pass
