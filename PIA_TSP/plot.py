import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
import random

def plot(x,y,TOURS):




	for tour in TOURS:
		solution = tour
		r = random.uniform(0, 1)
		r = math.floor(r*10)/10
		g = random.uniform(0, 1)
		g = math.floor(g*10)/10
		b = random.uniform(0, 1)
		b = math.floor(b*10)/10

		for i in range(0, int(len(solution))):
			if(i < int(len(solution))-1):
				connectpoints(x, y, solution[i], solution[i+1],r,g,b)

	plt.scatter(x,y,color='black',s=3)
	plt.scatter(x[0],y[0],color='red',s=50)

	plt.show()

def connectpoints(x, y, p1, p2,r,g,b):

	x1, x2 = x[p1], x[p2]
	y1, y2 = y[p1], y[p2]
	plt.plot([x1, x2], [y1, y2], 'k-', linewidth=.5, color = (r,g,b,1.0))

	
