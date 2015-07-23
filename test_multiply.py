import multiply as mp 

def test_multiply():
	"""
	Tests that the multiply function works
	"""
	assert mp.multiply(5,5) == 25
	assert mp.multiply(3,0) == 0
	assert mp.multiply(10,1) == 10