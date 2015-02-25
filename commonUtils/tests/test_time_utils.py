__author__ = 'x'

import unittest
from nose.tools import eq_, ok_, assert_in

from commonUtils.time_utils import TimeUtils


class get_Time(unittest.TestCase):
    def setUp(self):
        self.time = TimeUtils()

    def test_time(self):
        result1 = self.time.time_now()
        result2 = self.time.time_now()
        eq_(result1, result2)