
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
# from pylab import *
def get_array_of_values(url):
	array_of_values = []
	for line in urlopen(url):
		lineStr = str(line, encoding='utf8')
		lineStr = lineStr[(lineStr.find(",") + 1):-1]
		array_of_values.append(Decimal(lineStr))
	return array_of_values

def getAverage(values):
	total = 0
	for index in values:
		total += index
	return total / len(values)

get_array1 = get_array_of_values("https://coinbase.com/api/v1/prices/historical?page=1")
get_array2 = get_array_of_values("https://coinbase.com/api/v1/prices/historical?page=2")
get_array3 = get_array_of_values("https://coinbase.com/api/v1/prices/historical?page=3")
get_array = get_array1 + get_array2 + get_array3
plt.plot(get_array[::-1])
plt.ylabel('Price ($)')
plt.xlabel(str(getAverage(get_array)) + ' average')
plt.title('Bitcoin price over the last ' + str(len(get_array)) + ' blocks')
plt.show()