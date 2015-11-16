class Utils:
	def __init__(self):
		pass
	@staticmethod
	def parseFile(_filePath,_type):
		with open(_filePath) as _signalFile:
                        _lines = _signalFile.readlines()
                        _data = []
                        for _line in _lines:
                                _dataline = _line[:-1].split(",")
				_data.append( map(float,_dataline))#TODO:CHANGE THIS FOR DATATYPE
                        return _data
