__author__ = 'x'

from datetime import datetime


class TimeUtils(object):
    def __init__(self):
        current_time = ''

    def time_now(self):
        print datetime.now().time()
        return datetime.now().time()


