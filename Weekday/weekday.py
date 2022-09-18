"""

#~For Kids Challenges~#
Your task is easy, write a function that takes an date in format d/m/Y(String) and return what day of the week it was(String).
Example: "21/01/2017" -> "Saturday", "31/03/2017" -> "Friday"
Have fun!
"""
from datetime import datetime,date
def day_of_week(dates):
    d=datetime.weekday(datetime.strptime(dates,"%d/%m/%Y"))
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return days[d]



assert(day_of_week("08/12/2015")== "Tuesday")
assert(day_of_week("28/07/2014")== "Monday")
assert(day_of_week("29/02/2016")== "Monday")
assert(day_of_week("01/03/2016")== "Tuesday")
assert(day_of_week("28/02/1900")== "Wednesday")
assert(day_of_week("01/03/1900")== "Thursday")
print("done")