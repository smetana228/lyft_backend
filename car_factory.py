from battery.nubbin_battery import NubbinBattery 
from battery.spindler_battery import SpindlerBattery 
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughByEngine
from car import Car

class CarFactory:
	@staticmethod
	def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = CapuletEngine(last_service_mileage, current_mileage)
		battery = SpindlerBattery(current_date, last_service_date)
		car = Car(engine,battery)

		return car

	@staticmethod	
	def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = WilloughByEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(current_date, last_service_date)
		car = Car(battery,engine)

		return car

	@staticmethod	
	def create_palindrome(current_date, last_service_date, warning_light_on):
		engine = SternmanEngine(warning_light_on)
		battery = SpindlerBattery(current_date, last_service_date)
		car = Car(battery,engine)

		return car 

	@staticmethod	
	def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = WilloughByEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)
		car = Car(battery,engine)

		return car 

	@staticmethod	
	def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = CapuletEngine(last_service_mileage, current_mileage)
		battery = NubbinBattery(current_date, last_service_date)
		car = Car(battery,engine)

		return car  