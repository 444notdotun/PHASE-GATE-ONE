import unittest
from check_out_function import *
class test_check_out_function(unittest.TestCase):
	def test_that_sub_total_function_returns(self):
		expected = 5000
		actual = sub_total(5000,0)
		self.assertEqual(expected,actual)
	
	def test_that_sub_total_adds_more_value(self):
		sub_total(5000,0)
		sub_total(1000,5000)
		expected = 7000
		actual = sub_total(1000,6000)
		self.assertEqual(expected,actual)

	def test_that_vat_price_returns(self):
		expected = 525
		actual = vat_price(7000)
		self.assertEqual(expected,actual)

	def test_that_total_amount_returns(self):
		expected = 7525
		actual = total_amounts(7000,525)
		self.assertEqual(expected,actual)

	def test_that_balance_returns(self):
		expected = -525
		actual = balance(7525,7000)
		self.assertEqual(expected,actual)

	def test_that_balance_returns_zero(self):
		expected = 0
		actual = balance(7525,7525)
		self.assertEqual(expected,actual)
	def test_that_balance_returns_positive(self):
		expected =2
		actual = balance(7525,7527)
		self.assertEqual(expected,actual)

	def test_that_transaction_status_returns_payment_unsuccessful(self):
		expected = "payment unsuccessful!, come back when you are bouyant"
		actual = transaction_status(-525)
		self.assertEqual(expected,actual)

	def test_that_transaction_status_returns_payment_successful(self):
		expected = "payment successful, thank you for shopping"
		actual = transaction_status(0)
		self.assertEqual(expected,actual)
		
			
	
		