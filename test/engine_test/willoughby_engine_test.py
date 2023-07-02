import unittest

from engine.willoughby_engine import WilloughByEngine

class TestWilloughByEngine(unittest.TestCase):

	def test_needs_service_true(self):
		current_mileage = 80000
		last_service_mileage = 10000
		engine = WilloughEngine(current_mileage, last_service_mileage)

		self.assertTrue(engine.needs_service())

	def test_needs_service_true(self):
		current_mileage = 80000
		last_service_mileage = 30000
		engine = WilloughEngine(current_mileage, last_service_mileage)

		self.assertFalse(engine.needs_service())