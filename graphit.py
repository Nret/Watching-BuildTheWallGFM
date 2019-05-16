#!python3-32

import matplotlib.pyplot as plt
import datetime
import pylab
import csv

x = []
y = []

with open("log.csv") as csvfile:
	plots = csv.reader(csvfile)
	for row in plots:
		y.append(int(row[0][1:].replace(',', '')))
		x.append(row[1].trim())
		
# bars = plt.bar(x,y)
# Add labels above bars
# for bar in bars:
# 	yval = bar.get_height()
# 	plt.text(bar.get_x(), yval + .005, str(yval))
#autolabel(ax.patches)
# plt.plot(x,y)
# plt.scatter(x,y)
dates = [datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in x]
plt.plot_date(pylab.date2num(dates),y)
plt.xlabel('Time')
plt.ylabel('Money')
plt.title('TheTrumpWall GoFundMe Amount')
# tilt xlabels
plt.gcf().autofmt_xdate()
plt.show()
