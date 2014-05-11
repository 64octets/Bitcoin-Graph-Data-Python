
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen

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

def percent(num, total):
	return str(int((num/total) * 100)) +'%' 

base_string = "https://coinbase.com/api/v1/prices/historical?page="
strings = []
data = []

print("How many blocks to get info on? (per 1000)")
inpu = int(input())

print('Fetching data')
for num in range(inpu):
	strings.append(base_string + str(num))

counter = 1
for string in strings:
	data.append(get_array_of_values(string))
	print('Found 1000 blocks of data: (' + str(counter) +'/'+ str(inpu) + ') ' + percent(counter, inpu))
	counter += 1
final_data = []

print('Data imported successfully')
for values in data:
	final_data += values

print('Plotting Data')	
fig = plt.figure(figsize=(16, 5.5))
fig.subplots_adjust(left=0.06)
fig.subplots_adjust(right=0.97)
plt.plot(final_data[::-1])
plt.ylabel('Price ($)')
plt.xlabel(str(getAverage(final_data)) + ' average')
plt.title('Bitcoin price over the last ' + str(len(final_data)) + ' blocks')
plt.autoscale(True)

plt.show()