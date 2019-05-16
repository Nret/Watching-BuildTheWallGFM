#!python3-32

import csv

with open("log.txt") as file:
	reader = csv.reader(file, delimiter="@")
	data = [[r.strip() for r in row] for row in reader]
	# print(data)
	
with open("log.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerows(data)
