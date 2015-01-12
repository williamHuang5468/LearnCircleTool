# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from datetime import date
import sys

def countLearnCirlce(date, itemName):
	days = [0,1,2,3,4,5,6]
	result = []
	for item in days:
		result.append((date + timedelta(days=item)).strftime('%Y/%m/%d'))
	return result

def getTitle(date):
	days = [0,6]
	result = []
	for item in days:
		result.append((date + timedelta(days=item)).strftime('%Y/%m/%d'))
	first = "每週練習:".decode('utf-8')
	resultString = "%s%s~%s" %(first, result[0],result[1])
	return resultString

if __name__ == '__main__':
	separated = "-"
	input = sys.argv[1].split(',')
	itemName = ["閱讀，句子分段 30Min", "聽力，Echo Method，15Min"]
	date = datetime(int(input[0]), int(input[1]), int(input[2]))
	result = countLearnCirlce(date, itemName)
	resultString = getTitle(date)
	print resultString
	for item in result:
		print "%s%s%s"%(item, separated, itemName[0].decode('utf-8'))
		print "%s%s%s"%(item, separated, itemName[1].decode('utf-8'))