from datetime import datetime
from datetime import timedelta
from datetime import date
import sys

def countLearnCirlce(date, itemName):
	days = [1,3,7,15,31,63,127,255,511,1023]
	result = []
	for item in days:
		result.append((date + timedelta(days=item)).strftime('%Y-%m-%d'))
	return result

if __name__ == '__main__':
	separated = "~~"
	input = sys.argv[1].split(',')
	itemName = sys.argv[2]
	date = datetime(int(input[0]), int(input[1]), int(input[2]))
	result = countLearnCirlce(date, itemName)
	for item in result:
		print "%s%s%s"%(item, separated, itemName)