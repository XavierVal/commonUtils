__author__ = 'x'

from datetime import datetime


class TimeUtils(object):
    def __init__(self):
        self.current_time = ''

    def time_now(self):
        self.current_time = datetime.now().time()
        print "Current Time is: {}".format(self.current_time)
        return self.current_time


