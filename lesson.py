class Phone:
	def __init__(self, number, model, weight):
		self.number = number
		self.model = model
		self.weight = weight
	def Sinit(self, number, model):
		self.number = number
		self.model = model
		print(self.number, self.model)
	def Dinit(self): 
		pass
	def reseiveCall(self, name):
		print(f'Звонит {name}')
	def getNumber(self):
		return self.number
Phone1 = Phone('89112345678', 'Iphone', 150)
Phone2 = Phone('89119876543', 'Samsung', 160)
Phone3 = Phone('89113223143', 'Xiaomi', 170)
Phone1.reseiveCall('Олег'); print(Phone1.getNumber())
Phone2.reseiveCall('Степа'); print(Phone2.getNumber())
Phone3.reseiveCall('Паша'); print(Phone2.getNumber())

Phone4 = Phone('89112345611', 'Isung', 120)
print(Phone4.Sinit('89112345611', 'Isung'))

Phone5 = Phone('89112344611', 'Samphone', 210)
print(Phone5.Dinit())

