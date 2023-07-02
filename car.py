from servicable import Servicable

class Car(Servicable):

	def __init__(self, battery, engine):
		self.battery = battery
		self.engine = engine

	def needs_service(self):
		return self.engine.needs_service() or self.battery.needs_service()
		