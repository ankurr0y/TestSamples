def my_sample_function(test_variable):
	print(test_variable)
	return test_variable+1

def test_sample_function_that_passes():
	assert my_sample_function(3)==4

def test_sample_function_that_fails():
	assert my_sample_function(1)==4
