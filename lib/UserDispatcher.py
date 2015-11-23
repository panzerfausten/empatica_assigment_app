import json
class UserDispatcher:
	def __init__(self):
		_u1 =  User(1,"Darien Miranda",26,"dmiranda@empatica.com","pwd123","patient",["95f412","40bba7"])
		_u2 =  User(2,"Alberto Bojorquez",26,"aboj@empatica.com","bojo","patient",["efbaa7","57bba7"])
		_u3 =  User(3,"Mike Rodriguez",32,"mike@empatica.com","rodri","support",[])
		_u4 =  User(4,"God Juarez",9999999,"god@empatica.com","dioeilmiopastore","god",[])
		_u5 =  User(5,"Dr. Gordon Freeman",39,"gfreeman@empatica.com","wololo","doctor",[],patients =[_u1,_u2])
		self.users = {1:_u1,2:_u2,3:_u3,4:_u4,5:_u5}
	#dummy auth method
	def login(self,_user,_pass):
		for _x in self.users:
			if self.users[_x].username == _user and _pass == self.users[_x].password:
				return self.users[_x].toJson()
		return None
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
	def getAll(self,_json=True):
		if(_json):
			return json.dumps(self.users)
		else:
			return self.users
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
	def __init__(self,id,name,age,username,password,type,devices,patients = ""):
		self.id = id
		self.name = name
		self.username = username
		self.password = password
		self.age = age
		self.type = type
		self.devices = devices
		self.patients = patients
		
	def toJson(self):
		if(self.patients != None):
			_patients = []
			for _p in self.patients:
				_patients.append(_p.name)
			return json.dumps({"id":self.id,"name":self.name,"age":self.age,"type":self.type,"devices":self.devices,"patients":_patients}, sort_keys=True, indent=4)
		else:
			return json.dumps({"id":self.id,"name":self.name,"age":self.age,"type":self.type,"devices":self.devices,"patients":self.patients}, sort_keys=True, indent=4)
