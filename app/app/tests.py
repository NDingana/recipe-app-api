
"""we're going to import the Django TestCase The test case is a class that comes with Django 
that basically has a bunch of helper functions that help us test our Django code. """
from django.test import TestCase

"""Next we're going to import the function that we're going to test"""
from app.calc import add



"""Create the test class that we want to use so and 
we're going to call it CalcTests and we're going to inherit from the TestCase"""
class CalcTests(TestCase):

    """The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class.
    
    one thing to mention about this function name is that just like when Django searches for the files 
    that begin with tests, the test functions must all begin with test because 
    if you were to change this function name to add_numbers, 
    you would put like some test then it wouldn't run this test when we actually run our Django tests.
    
    """
    def test_add_numbers(self):

        """Test that values are added together
        we're going to use an assertion here so a test is set up of two components there's 
        usually the set up stage which is where you would set your set your function up to be tested and 
        then there's the assertion which is when you actually test the output and 
        you confirm that the output equals what you expected it equal."""
        self.assertEqual(add(3, 8), 11)