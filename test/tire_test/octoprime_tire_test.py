import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
	def test_needs_service_ture(self):
		tires = [0.8,0.8,0.9,0.9]
		tire = OctoprimeTire(tires)

		self.assertTrue(tire.needs_service())
	def test_needs_service_false(self):
		tires = [0.6,0.6,0.6,0.6]
		tire = OctoprimeTire(tires)

		self.assertFalse(tire.needs_service())		
