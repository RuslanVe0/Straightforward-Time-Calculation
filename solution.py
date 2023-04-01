from math import ceil, floor
from calendar import monthrange

"""
------------------------------------------
A straightforward solution to the problem.
In order to find - fast and reliable solution, and rational approach to the problem. 
We need to divide time into smaller parts - each day consists of 24-hour, which is 12*2=24.
If time is bigger than 24, thus it should add to day += 1, each month, if not months 
that does not consists 31-days, are (15 + 15)+1 days in one year.
There are 12-months, consisting of 4-weeks, which is approximately 52-weeks per year
, and that is equivalent to 365, due to the fact  that 48-weeks in days are
(each week consists of 7-days) * 7, is approximately 365-days per year.
In order to solve that problem, and reduce its complexity, we need to find the sum of all - 


	-> months in the year,
		weeks of each months,
			days in each months.
	-> h:m:s (where h=hours, m=minutes, s=seconds) of each day (<=> i.e 24-hoursd).
		check hours,
			check minutes,
				check seconds,


We'll basically need this, the sum of weeks in a month, in order to know WHETHER to use 
next month. If current week is 3, and month consists of 
3-weeks and today is the last day of the month, thus ... if hour is >= 24, it'll
change to 0, and month + 1, thus if february it'll become march, and will do that again.
We'll start by finding current year, then we need to find if it is a leap year, thus if leap year - 366-days otherwise -> 365(-1).
"""

class solution(object):
    def __init__(self, year:int, day:int, total_days:int, total_hours_day:int, pool:dict, add_hour:int) -> (int, int, int, int, dict):
        #self.initial = pool["hour"]
        self.year = year; self.day = day; self.total_days = total_days; self.total_hours_day = total_hours_day; self.pool = pool
        self.pool["hour"] = self.pool["hour"]+add_hour
    
    def create_pool(self:object):
        ol = self.find_hours() # in order to find - h, and if required to change month.
        return self.pool
    
    def find_hours(self:object):
        while self.pool["hour"] >= 24:
            hour_lamb = lambda x: x-24 if (24-x) > 0 else (x-24) # if hour is > 24, thus it'll (24-x), where x = defined hour.
            once = hour_lamb(self.pool["hour"])
            self.pool["hour"], self.pool["day"] = once, self.find_day(self.pool["day"]+1)
            self.pool["minute"], self.pool["second"] = self.find_m_and_second(self.pool["minute"], self.pool["second"])
    
    def find_m_and_second(self:object, minute:int, second:int) -> (int, int):
        #minute, second = [minute, 1] if second >= 60 else [minute, second+1]
        minute, second, self.pool["hour"] = [1,1, self.pool["hour"]+1] if minute >= 60 else [minute, second, self.pool["hour"]]
        return minute, second

    def find_day(self:object, tolook_day:int):
        last_day_month = monthrange(self.pool["year"], self.pool["month"])[1]
        if tolook_day > last_day_month:
            self.pool["day"], self.pool["month"] = 1, self.find_month(self.pool["month"]+1)
            return 1
        return tolook_day
    
    def find_month(self:object, tolook_month:int):
        if tolook_month > 12:
            self.pool["month"], self.pool["year"] = 1, self.pool["year"]+1
            return 1
        return tolook_month

if __name__ == "__main__":
    instance = solution(year=2023, day=31, total_days=365, total_hours_day=24, pool={"year":2023, "month":4, "day":1, "hour":16, "minute":29, "second":49}, add_hour=14000).create_pool()
    print(instance)

