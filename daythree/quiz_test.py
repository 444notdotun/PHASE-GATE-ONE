import unittest
from quiz_function import *
class test_quiz_function(unittest.TestCase):
	def test_that_questioner_exit(self):
		questioner
	def test_that_questioner_returns_different_element_in_an_array(self):
		expected=questioner()
		
		self.assertNotEqual(expected,questioner())
	def test_that_question_index_exist(self):
		question_index
	def test_that_question_index_returns_index_of_question(self):
		yes = questioner()
		new = questions.index(yes)
		another = question_index(yes)
		self.assertEqual(another,new)
		
	def test_that_answers_exist(self):
		answer
	def test_that_answer_gives_diff_answers(self):
		yes = questioner()
		list = question_index(yes)
		new = answer(yes)
		another = new[3]
		expected = answers[list]
		self.assertEqual(another,expected)
	def test_that_validation_exist(self):
		validation
	
	

		
		