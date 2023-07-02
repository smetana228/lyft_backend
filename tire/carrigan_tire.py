from tire.tire import Tire

class CarriganTire(Tire):

	def __init__(self,tires):
		self.tires=tires

	def needs_service(self):
		for x in self.tires:
			if x >= 0.9:
				return True
		return False
