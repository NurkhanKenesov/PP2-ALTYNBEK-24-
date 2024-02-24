#ex1
import datetime
print(datetime.date.today() - datetime.timedelta(days = 5))
#ex2
import datetime
print("Today is: ",datetime.date.today())
print("Tomorrow is: ",datetime.date.today()+datetime.timedelta(1))
print("Yesterday was:",datetime.date.today()-datetime.timedelta(1))
#ex3
import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)
#ex4
import datetime
def date_diff(dt2:datetime.date,dt1:datetime.date) -> (int|float):
    diff = dt2 - dt1
    return abs(diff.days*24*3600 + diff.seconds)
DateA = datetime.date(2020,12,2)
DateB = datetime.date(2023,12,2)
print(f"There is {date_diff(DateA,DateB)} seconds between {DateA} and {DateB}" )