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
	def getHeatMapSessions(self,_json=True):
		_h = []
		_e = []
		_t = []
		_nSessions = 0 
		_x = 0
		for _folder in reversed(os.listdir(self._dataFolder)):
			for _device in self.devices:
				if _device in _folder: #get only the folders from his/her device
					_file = self._dataFolder + _folder 
					_d = Session(_file)
					_mdata = _d.getMetaDataOnly()
					_avgHR = _mdata["session"]["statistics"]["HR_avg"]
					_avgEDA = _mdata["session"]["statistics"]["EDA_avg"]
					_avgTEMP = _mdata["session"]["statistics"]["TEMP_avg"]
					_HM_HR= {}
					_HM_EDA= {}
					_HM_TEMP= {}
					if(_avgHR > 90):
						_HM_HR["sessionId"] = _folder 
						_HM_HR["date"] = int(_folder[:-7])
						_HM_HR["value"] = 60 + _x #silly hack to get links on the heatmap
					else:
						_HM_HR["sessionId"] = _folder 
						_HM_HR["date"] = int(_folder[:-7])
						_HM_HR["value"] = 2 + _x 
					print _HM_HR
					_h.append(_HM_HR)
					if(_avgEDA > 5):
						_HM_EDA["sessionId"] = _folder 
						_HM_EDA["date"] = int(_folder[:-7])
						_HM_EDA["value"] = 60 + _x 
					else:
						_HM_EDA["sessionId"] = _folder 
						_HM_EDA["date"] = int(_folder[:-7])
						_HM_EDA["value"] = 2+ _x 
					_e.append(_HM_EDA)
					if(_avgTEMP > 37.5):
						_HM_TEMP["sessionId"] = _folder 
						_HM_TEMP["date"] = int(_folder[:-7])
						_HM_TEMP["value"] = 60+ _x 
					else:
						_HM_TEMP["sessionId"] = _folder 
						_HM_TEMP["date"] = int(_folder[:-7])
						_HM_TEMP["value"] = 2+ _x 
					_t.append(_HM_TEMP)
					_x +=1

		if(_json):
			return [json.dumps(_h),json.dumps(_e),json.dumps(_t)]
		else:
			return [_HM_HR,_HM_EDA,_HM_TEMP]
	def getSupportSession(self,session):
		pass	

	def getDataFromSession(self,session,signalType,_json=True):
		_file = self._dataFolder +session
		_d = Session(_file)
		return _d.getData(signalType,_json)
	def getDataByDate(self,session,signals):
		pass
