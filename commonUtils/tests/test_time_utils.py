__author__ = 'x'

import unittest
from nose.tools import eq_, ok_, assert_in, assert_greater, assert_almost_equal, assert_not_equal
import time

from commonUtils.time_utils import TimeUtils


class TimeGetCurrentTime(unittest.TestCase):
    def setUp(self):
        self.time_obj = TimeUtils()
        self.result1 = self.time_obj.time_now()
        self.result2 = self.time_obj.time_now()

    def test_time_equal(self):
        eq_(self.result1, self.result2, "Time does not match")

    def tearDown(self):
        pass


class TimeGetTimeDelayed(unittest.TestCase):
    def setUp(self):
        self.time_obj = TimeUtils()
        self.time1 = self.time_obj.time_now()

    def test_time_delayed(self):
        time.sleep(1)
        time2 = self.time_obj.time_now()
        assert_not_equal(self.time1, time2, "Time was not incremented")

    def tearDown(self):
        pass
