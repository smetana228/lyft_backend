import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
	def test_needs_service_ture(self):
		tires = [0.6,0.7,0.8,0.9]
		tire = CarriganTire(tires)

		self.assertTrue(tire.needs_service())
	def test_needs_service_false(self):
		tires = [0.6,0.6,0.8,0.8]
		tire = CarriganTire(tires)

		self.assertFalse(tire.needs_service())		
