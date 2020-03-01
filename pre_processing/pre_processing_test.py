"""Test"""
import unittest
from pre_processing.pre_processing import PreProcessor


class TestMyModule(unittest.TestCase):
    """Test Module"""

    def setUp(self):
        """Setup"""
        return

    def test_do_divide(self):
        """Do Test"""
        first_arg = "@my_handler here is my tweet http://www.columbia.com"

        result = PreProcessor().pre_process_text(first_arg)

        expected_result = [231, 34, 31, 276, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(result, expected_result)
        