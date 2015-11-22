from datetime import datetime
import math
class Utils:
	def __init__(self):
		pass
	@staticmethod
	def secsToHMS(seconds):
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)
	def daysAgo(self,unixTime):
		_now = datetime.now()
		_sTime = datetime.fromtimestamp(unixTime)
		_delta = (_now - _sTime)
		return str(_delta.days)
	@staticmethod
        def groupBySec(data,_startTime, _duration,avg=False , _max=False,timeStamp=True):
                _data = [None] * _duration
		print len(data)
                for _v in data:
                        if (len(str(_v[0])) > 10):
                                _pos = int(math.floor(( int( str(_v[0])[:10]) - _startTime)))
                        else:
                                _pos = int(math.floor((_v[0] - _startTime)))
                        if(_pos > 1 and _pos < len(_data) -1):
                                if(_data[_pos-1] == None):
                                        _data[_pos-1] = []
                                        _data[_pos-1].append(_v)
                                else:
                                        _data[_pos-1].append(_v)

                if(avg):
                        _avgs = [None] * _duration
                        for _x,_d in enumerate(_data):
                                _total = 0.0
                                if not (_d == None):
                                        for _v in _d:
                                                _total += _v[1]
                                        _avg = _total / len(_d)
					if (timeStamp):
						_avgs[_x] = [_startTime+(_x)]
						_avgs[_x].append(_avg)
					else:
						_avgs[_x] = _avg
                        return filter(None,_avgs)
	@staticmethod
	def toPrettyDate(unixTime):
		_dt = datetime.fromtimestamp(unixTime)
		return "%i/%i/%i" %(_dt.day,_dt.month,_dt.year)
