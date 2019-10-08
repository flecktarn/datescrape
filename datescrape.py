import sys
import datetime
import re

def parseWeekDay(dayString):
	#returns the day number (from 0 to 6) from a string representing the day.
	dayIndex = [['m','mon','monday'],\
			   ['tu','tue','tues','tuesday'],\
			   ['w','wed','wednesday'],\
			   ['th','thurs','thursday'],\
			   ['f','fri','friday'],\
			   ['sat','saturday'],\
			   ['sun','sunday']]

	for i in range(len(dayIndex)):
		for j in range(len(dayIndex[i])):
			if dayIndex[i][j] == dayString.lower():
				return i

	return -1


def parseMonth(monthString):
	#returns the month number (from 0 to 11) from a string representing the month.
	monthIndex = [['jan','january'],\
  			     ['feb','februaru'],\
  			     ['mar','march'],\
  			     ['apr','april'],\
  			     ['may'],\
  			     ['jun','june'],\
  			     ['jul','july'],\
  			     ['aug','august'],\
  			     ['sep','sept','september'],\
  			     ['oct','october'],\
  			     ['nov','november'],\
  			     ['dec','december']]
					
	for i in range(len(monthIndex)):
		for j in range(len(monthIndex[i])):
			if monthIndex[i][j] == monthString.lower():
				return i

	return -1

try:
	parseMe = sys.argv[1]
except IndexError:
	print(f"Error, expected 1 argument, received {len(sys.argv)-1}")
	exit()

#initialize date
date = [0,0,0]

#cases:
#date formatted like: 1(st) Jan(uary) 2019
format1 = r"^[\s]*([\d]+)[\w]+[\s]+([\w]*)[\s]+([\d]*)[\s]*$"

#date formatted like: Jan(uary) 1(st) 2019
format2 = r"^[\s]*([a-z]+)[\s]+([\d]+)[\w]*[\s]*([\d]*)[\s]*$"

#date formatted like: 1 1 2019
format3 = r"^[\s]*([\d]*)[\s]*([\d]*)[\s]*([\d]+)[\s]*$"

#next tuesday, last monday
format4 = r"^[\s]*(next|last)[\s]*([\w]*)[\s]*$"

#print(parseWeekDay(parseMe))
print(parseMonth(parseMe))



