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


def parseTime(timeString):

	#takes a string representing time, returns an array of [Hours, Minutes, Period]
	#Period is 0 if AM, 1 if PM, 2 if 24H time (defaults to 24H time)

	query = r'^[\s]*([\d:]+)[\s]*([\w]*)[\s]*$'

	matched = re.match(query, timeString)

	if not matched:
		print("Error. Could not parse a valid time, ensure you format correctly.")
		return

	matches = matched.groups()

	if matches[0] == "":
		print("Error. Could not parse a valid time.")
		#no time was found
		return
	else:
		timeMatch = matches[0]


	colons = timeMatch.count(":")


	if colons == 0:
		maxLength = 4

	elif colons == 1:
		maxLength = 5

	else:
		#invalid time
		print("Error. Inappropriate use of ':',  should be in the form HH:MM")
		return 

	if len(timeMatch) > maxLength:
		print("Error. Inappropriately formatted time string. Time string too long.")

	if colons == 1:
		#split hours and minutes by the colon
		timeArray = timeMatch.split(":")

		for i in range(len(timeArray)):
			timeArray[i]=int(timeArray[i])

	else:
		#handle length of time string
		if(len(timeMatch) in [1,2]):
			hours = int(timeMatch)
			minutes = 0


		elif(len(timeMatch) == 3):
			hours = int(timeMatch[0])
			minutes = int(timeMatch[1:])


		else:
			hours = int(timeMatch[0:2])
			minutes = int(timeMatch[2:])

		
		if hours > 23:
			print("Error. Invalid value. Hours cannot exceed 23")
			return
		if minutes > 59:
			print("Error. Invalid value. Minutes cannot exceed 59")
			return
		timeArray = [hours,minutes]



	periodMatch = matches[1]

	if periodMatch.lower() in ['a','am']:
		period = 0
		if timeArray[0] == 0:
			timeArray[0] = 12

	elif periodMatch.lower() in ['p','pm']:
		period = 1

	else:
		#24H clock
		period = 2  


	timeArray += [period]

	print(timeArray)

	return timeArray










#initialize date
date = [0,0,0]


def parseDate(dateString):

	#cases:
	#date formatted like: 1(st) Jan(uary) 2019
	format1 = r"^[\s]*([\d]+)[a-z]*[\s]+([a-z]+)[\s]*([\d]*)[\s]*$"

	#date formatted like: Jan(uary) 1(st) 2019
	format2 = r"^[\s]*([a-z]+)[\s]+([\d]+)[\w]*[\s]*([\d]*)[\s]*$"

	#date formatted like: 1 1 2019
	format3 = r"^[\s]*([\d]*)[\s]*([\d]*)[\s]*([\d]+)[\s]*$"

	#next tuesday, last monday
	format4 = r"^[\s]*(next|last)[\s]*([\w]*)[\s]*$"

	formats = [format1,format2,format3,format4]



	matchList = [[],[],[],[]]

	for i in range(len(formats)):
		matched = re.match(formats[i],dateString)
		if matched:
			matchList[i] = matched.groups()


	bestMatch = matchList[0]
	bestMatchCount = 0

	for i in matchList:
		matchCount = len(i)
		if matchCount > bestMatchCount:
			bestMatchCount = matchCount
			bestMatch = i

	#print(bestMatch)
	return bestMatch



#print(parseWeekDay(parseMe))
#print(parseMonth(parseMe))

try:
	parseMe = sys.argv[1] 
	print(f'query = "{parseMe}"')
except IndexError:
	print(f"Error, expected 1 argument, received {len(sys.argv)-1}")
	exit()


#parseMeList = parseMe.split("@")
print(parseDate(parseMe))









