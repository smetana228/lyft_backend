from tire.tire import Tire

class CarriganTire(Tire):

	def __init__(self,tires):
		self.tires=tires

	def needs_service(self):
		tires_worn=0
		for x in tires:
			tires_worn=+x
		return tires_worn <= 3.6