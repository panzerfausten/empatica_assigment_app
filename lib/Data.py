from UserDispatcher import UserDispatcher
from Utils import Utils
import os
class Data:
	def __init__(self,userId,device=None):
		_userDispatcher = UserDispatcher()
		self._dataFolder = "../data"
		self.userId = userId
		self.user = _userDispatcher.get(userId,False)
		self.device = device 
		#if there is no provided device, fallback to the first device
		if(self.device == None):
			self.device = self.user.devices[0]
	def getSessions(self,json=True):
		for _folder in os.listdir(self._dataFolder):
			if self.device in _folder: #get only the folders from his/her device
				print _folder
	def getDataFromSession(self,session,signalType):
		_file = self._dataFolder +"/"+session+"/"+signalType+".csv"
		return Utils.parseFile(_file,signalType)
	def getDataByDate(self,session,signals):
		pass
