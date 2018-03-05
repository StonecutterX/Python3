#
# difference between @staticmethod and @classmethod
#
# @authors: xiangsun
# https://stackoverflow.com/questions/12179271/
# meaning-of-classmethod-and-staticmethod-for-beginner/12179325#12179325
#

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def printTime(self):
        print("{}/{}/{}".format(self.year, self.month, self.day))

    # it's about class itself, not an instance of the class
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    # without access to the object and its internals
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('08-08-2008')
date2.printTime()
is_date = Date.is_date_valid('08-08-2008')
