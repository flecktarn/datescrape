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

try:
	parseMe = sys.argv[1]
except IndexError:
	print(f"Error, expected 1 argument, received {len(sys.argv)-1}")
	exit()

#initialize date
date = [0,0,0]

#cases:
#date formatted like: 1(st) January 2019
format1 = r"([\d]+)[\w]*[\s]*([\w]*)[\s]*([\d]*)"

#date formatted like: 1 1 2019
format2 = r"^[\s]*([\d]*)[\s]*([\d]*)[\s]*([\d]*)[\s]*$"

#next tuesday, last monday
format3 = r"(next|last)[\s]*([\w]*)"




print(parseWeekDay(parseMe))