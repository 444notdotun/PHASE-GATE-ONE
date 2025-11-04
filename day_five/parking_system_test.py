import unittest
from parking_system_function import*
class test_parking_system_function(unittest.TestCase):
	def test_that_check_for_slot_returns_position_of_parked_car(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		expected = 0
		actual = check_for_slot("adedotun",parking_slot)
		self.assertEqual(expected,actual)

	def test_that_check_for_slot_returns_there_is_no_available_parking_slot(self):
		parking_slot=[1,2,3,4,5,3,2,3,44,2,2,3,2,21,3,4,1,2,3,8]
		expected ="There is no available parking slot"
		
		actual = check_for_slot("adedotun",parking_slot)
		self.assertEqual(expected,actual)

	def test_that_check_for_slot_adds_more_than_one_car(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

		expected = 0
		actual = check_for_slot("adedotun",parking_slot)
		self.assertEqual(expected,actual)
		expected = 1
		actual = check_for_slot("ade",parking_slot)
		self.assertEqual(expected,actual)
		
	
	def test_that_retrieve_parked_car_returns_hope_to_see_you_soon(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		check_for_slot("adedotun",parking_slot)
		expected = "THANK YOU AND HOPE TO SEE YOU SOON"
		actual = retrieve_parked_car("0","adedotun",parking_slot)
		self.assertEqual(expected,actual)

	def test_that_retrieve_parked_car_returns_enter_a_valid_name(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		check_for_slot("adedotun",parking_slot)
		expected = "ENTER A VALID KEY"
		actual = retrieve_parked_car("0","ade",parking_slot)
		self.assertEqual(expected,actual)

	def test_that_retrieve_parked_car_returns_enter_a_valid_key(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		check_for_slot("adedotun",parking_slot)
		expected = "ENTER A VALID KEY"
		actual = retrieve_parked_car("8","adedotun",parking_slot)
		self.assertEqual(expected,actual)
	def test_that_show_parking_lot_works(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		expected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		actual = show_parking_lot(parking_slot)
		self.assertEqual(expected,actual)

	def test_that_show_parking_lot_shows_its_occupied(self):
		parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		check_for_slot("adedotun",parking_slot)
		expected = ["adedotun",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		actual = show_parking_lot(parking_slot)
		self.assertEqual(expected,actual)


