import csv

file = open('eur-usd.csv')
csv_reader = csv.DictReader(file)
memoryDimension = 3
values = [ float(el['Ultimo'].replace(',', '.')) for el in csv_reader ]
result = []

for i in range(memoryDimension, len(values)):
	result.append( sum(values[i - memoryDimension: i]) / memoryDimension )

print (result)