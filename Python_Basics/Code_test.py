# Each code sample should run separately. Comment out the others.
import unittest
from code_test_target import title_string, AddOne

# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIn(item, list)
# assertNotIn(item, list)

# Test a function
class FunctionTestCase(unittest.TestCase):
    """Tests for 'code_test_target.py'."""
    def test_title_string(self):
        """Check is it the same"""
        ret_string = title_string("afadf fafdas")
        self.assertEqual(ret_string, "Afadf Fafdas")
    def test_title_string2(self):
        """Check is it the same"""
        ret_string = title_string("123 fafa 1341")
        self.assertEqual(ret_string, "123 Fafa 1341")

unittest.main()

# Test a class
class ClassTestCase(unittest.TestCase):
    """Tests for 'code_test_target.py'."""
    def test_class_addone(self):
        add_one = AddOne()
        add_one.store_data(2)
        self.assertIn([2,3], add_one.saved_data)

unittest.main()

#
class ClassTestCase(unittest.TestCase):
    """Tests for 'code_test_target.py'."""
    def setUp(self):
        self.add_one = AddOne()
        self.input_data = [1,2,3,4,5]
        self.saved_data = [[1,2],[2,3],[3,4],[4,5],[5,6]]

    def test_class_addone(self):
        for item in self.input_data:
            self.add_one.store_data(item)
        for item in self.saved_data:
            self.assertIn(item, self.add_one.saved_data)

unittest.main()
