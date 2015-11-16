import json
class UserDispatcher:
	def __init__(self):
		_u1 =  User(1,"Darien",26,["95f412","40bba7"])
		_u2 =  User(2,"Darien",26,["95f412","40bba7"])
		self.users = {1:_u1,2:_u2}
	
	def get(self,userId,json=True):
		if (userId in self.users):
			if(json):
				return self.users[userId].toJson()
			else:
				return self.users[userId]
		else:
			if(json):
				return "{}"
			else:
				return []
	def getDevices(self,userId,jsn=True):
		if (userId in self.users):
			if(jsn):
				_devices = self.users[userId].devices
				return json.dumps(_devices)
			else:
				return self.users[userId].devices
		else:
			if(jsn):
				return "{}"
			else:
				return []
class User:
	def __init__(self,id,name,age,devices):
		self.id = id
		self.name = name
		self.age = age
		self.devices = devices
	def toJson(self):
		return json.dumps({"id":self.id,"name":self.name,"age":self.age,"devices":self.devices}, sort_keys=True, indent=4)
