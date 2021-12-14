import unittest
from easyneuron.data import load_random_humans, gen_stairs
from easyneuron._testutils import log_errors

class TestDataLoading(unittest.TestCase):

	@log_errors
	def test_random_humans(self):
		load_random_humans() # just try to run it to check for errors

class TestDataGen(unittest.TestCase):

	@log_errors
	def test_gen_stairs(self):
		gen_stairs(3, 2) # just try to run it to check for errors