from datetime import datetime
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
