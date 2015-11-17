import os
import json
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
	def parseMetadata(self,_lines,_type):
		_mdata = {"metadata":{}}
		if(_type == "ACC"):
			_startX,_startY,_startZ = map(float,_lines[0][:-1].split(","))
			_mdata["metadata"]["startTime"] = _startX
			_mdata["metadata"]["startX"] = _startX
			_mdata["metadata"]["startY"] = _startY
			_mdata["metadata"]["startZ"] = _startZ
			_freqX,_freqY,_freqZ = map(float,_lines[1][:-1].split(","))
			_mdata["metadata"]["freq"] = _freqX
			_mdata["metadata"]["freqX"] = _freqX
			_mdata["metadata"]["freqY"] = _freqY
			_mdata["metadata"]["freqZ"] = _freqZ
		if(_type == "HR" or _type == "EDA" or _type == "BVP"  or _type == "TEMP" or _type == "HR_qi"):
			_startTime = map(float,_lines[0][:-1].split(","))
			_freq = map(float,_lines[1][:-1].split(","))
			_mdata["metadata"]["startTime"] = _startTime[0]
			_mdata["metadata"]["freq"] = _freq[0]
		return _mdata
	def parseFile(self,_type):
		with open("%s/%s" %(self._sessionPath,self._filePaths[_type])) as _signalFile:
                        _lines = _signalFile.readlines()
                        _session = {"session":{"data":{}}}
			_mdata = self.parseMetadata(_lines,_type)
			_session["session"]["metadata"] = _mdata["metadata"]
			
			_data = []
                        for _i,_line in enumerate(_lines[self.cutLine(_type):]):
                                _dataline = _line[:-1].split(",")
				_timestamp = self.calcTimeStamp(_i,_mdata["metadata"]["freq"],_mdata["metadata"]["startTime"])
				_floatline = map(float,_dataline)
				_floatline.append(_timestamp)
				_data.append(_floatline[::-1])
			_session["session"]["data"][_type] = _data
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
