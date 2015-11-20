import os
import json
from Utils import Utils
class Session:
	def __init__(self,_sessionPath):
		self._sessionPath = _sessionPath
		self._filePaths = {}
		self.findFiles()
	def getData(self,_type,_json=True):
		if (_json):
			return json.dumps(self.parseFile(_type))
		else:
			return self.parseFile(_type)

	def getMetaDataOnly(self):
		return self.parseFile("EDA",_readAll=False)
	def parseMetadata(self,_lines,_type):
		_utils = Utils()		
		_mdata = {"metadata":{}}
		_mdata["metadata"]["id"] = self._sessionPath.replace("data/","")
		if(_type == "ACC"):
			_startX,_startY,_startZ = map(float,_lines[0][:-1].split(","))
			_mdata["metadata"]["startTime"] = _startX
			_endX,_endY,_endZ = map(float,_lines[-1][:-1].split(","))
			_mdata["metadata"]["endTime"] = _endX
			_mdata["metadata"]["startX"] = _startX
			_mdata["metadata"]["startY"] = _startY
			_mdata["metadata"]["startZ"] = _startZ
			_freqX,_freqY,_freqZ = map(float,_lines[1][:-1].split(","))
			_end = self.calcTimeStamp(len(_lines)-1,_freqX,_startX)
			_mdata["metadata"]["freq"] = _freqX
			_mdata["metadata"]["freqX"] = _freqX
			_mdata["metadata"]["freqY"] = _freqY
			_mdata["metadata"]["freqZ"] = _freqZ
			_mdata["metadata"]["prettyTime"] = Utils.secsToHMS(_endX - _startX)
			_mdata["metadata"]["prettyDaysAgo"] = _utils.daysAgo(_startX)
		if(_type == "HR" or _type == "EDA" or _type == "BVP"  or _type == "TEMP" or _type == "HR_qi"):
			_startTime = map(float,_lines[0][:-1].split(","))
			_freq = map(float,_lines[1][:-1].split(","))
			_mdata["metadata"]["startTime"] = _startTime[0]
			_mdata["metadata"]["freq"] = _freq[0]
			_end = self.calcTimeStamp(len(_lines)-1,_freq[0],_startTime[0])
			_mdata["metadata"]["endTime"] = _end
			_mdata["metadata"]["prettyTime"] = Utils.secsToHMS(_end - _startTime[0])
			_mdata["metadata"]["prettyDaysAgo"] = _utils.daysAgo(_startTime[0])
		_mdata["metadata"]["deviceId"] =  self._sessionPath[-6:]
		#_mdata["metadata"]["availableSignals"] = self._
		return _mdata
	def parseFile(self,_type,_readAll=True):
		with open("%s/%s" %(self._sessionPath,self._filePaths[_type])) as _signalFile:
                        _lines = _signalFile.readlines()
                        _session = {"session":{"data":{},"statistics":{}}}
			_mdata = self.parseMetadata(_lines,_type)
			_session["session"]["metadata"] = _mdata["metadata"]
			
			_data = []
			if(_readAll):
				for _i,_line in enumerate(_lines[self.cutLine(_type):]):
					_dataline = _line[:-1].split(",")
					_timestamp = self.calcTimeStamp(_i,_mdata["metadata"]["freq"],_mdata["metadata"]["startTime"])
					_floatline = map(float,_dataline)
					_floatline.append(_timestamp)
					_data.append(_floatline[::-1])
				_session["session"]["data"][_type] = _data
			else:
				_session = self.statistics(_session)
                        return _session
	def statistics(self,_session):
		with open("%s/%s" %(self._sessionPath,self._filePaths["EDA"])) as _signalFile:
			_avgD = []
                        _lines = _signalFile.readlines()
			for _x in range (self.cutLine("EDA"), len(_lines),120):
				_dataline = _lines[_x][:-1].split(",")
				_floatline = map(float,_dataline)
				_avgD.append(_floatline[0])
			_session["session"]["statistics"]["EDA_avg"] =  sum(_avgD) / len(_avgD)
		if ("HR" in self._filePaths):
			with open("%s/%s" %(self._sessionPath,self._filePaths["HR"])) as _signalFile:
				_avgD = []
				_lines = _signalFile.readlines()
				for _x in range (self.cutLine("HR"), len(_lines),120):
					_dataline = _lines[_x][:-1].split(",")
					_floatline = map(float,_dataline)
					_avgD.append(_floatline[0])
				_session["session"]["statistics"]["HR_avg"] =  sum(_avgD) / len(_avgD)
		else:
			_session["session"]["statistics"]["HR_avg"] = -1 #if there is no HR file return -1 
		return _session
	def findFiles(self):
		for _file in os.listdir(self._sessionPath):
			if(_file == "ACC.csv"):
				self._filePaths["ACC"] = _file
			if(_file == "BVP.csv"):
				self._filePaths["BVP"] =_file
			if(_file == "EDA.csv"):
				self._filePaths["EDA"] = _file
			if(_file == "HR.csv"):
				self._filePaths["HR"]    =_file
			if(_file == "HR_qi.csv"):
				self._filePaths["HR_qi"] =_file
			if(_file == "IBI.csv"):
				self._filePaths["IBI"]  = _file
			if(_file == "TEMP.csv"):
				self._filePaths["TEMP"] = _file
			if(_file == "tags.csv"):
				self._filePaths["tags"] = _file
	def cutLine(self,_type):
		if(_type == "HR" or _type == "EDA" or _type == "BVP"  or _type == "TEMP" or _type == "HR_qi"):
			return 2
	def calcTimeStamp(self,_i,_freq,_startTime):
		return _startTime + (_i / _freq)
