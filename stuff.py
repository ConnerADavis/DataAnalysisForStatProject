"""
Analysis to search for evidence of voter fraud in 2000 election. A fraudulent election would have the histogram results
smeared toward the top right.
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
bush = list()
turnout = list()
with open("bushturnout.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        bush.append(float(row[0]))
        turnout.append(float(row[1]))

bush = np.asarray(bush)
turnout = np.asarray(turnout)
hist, xedges, yedges = np.histogram2d(turnout, bush, 100)

xidx = np.clip(np.digitize(turnout, xedges), 0, hist.shape[0]-1)
yidx = np.clip(np.digitize(bush, yedges), 0, hist.shape[1]-1)
c = hist[xidx, yidx]
plt.scatter(turnout, bush, c=c)

plt.show()