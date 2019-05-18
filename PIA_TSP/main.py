import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import math

# Globals

data = [] 
POINTS = np.array((10,2))
LIMIT = 0
VISIT_TIME = []
TOURS = []
TOTAL_TIME = 0
DATASETS = [
'150_sitios_480',
'150_sitios_1200',
'100_sitios_1200',
'100_sitios_480',
'50_sitios_480',
'50_sitios_1200',
'75_sitio_480',
'75_sitio_1200'
]

def setData():

	global data, LIMIT, VISIT_TIME, POINTS

	X = []
	Y = []

	f = open("./Datasets_PIA_TSO_TSP/150_sitios_480.txt")
	for i, l in enumerate(f.readlines()):
		data.append(l.strip().split('\t'))

		if i >= 5:
			X.append(int(data[i][1]))
			Y.append(int(data[i][2]))
			VISIT_TIME.append(int(data[i][3]))
	
	r = np.array(X)
	s = np.array(Y)

	# Set global data

	POINTS = np.column_stack((X, Y))
	POINTS.reshape(len(POINTS),2)
	LIMIT = int((data[1][1]))
	VISIT_TIME[0] = 0

	f.close()

	# Call function
	nearestNeighbor()


def nearestNeighbor():
	f = 0
	while f < 1:

		x = []
		y = []

		for i in POINTS:
			x.append(i[0])
			y.append(i[1])

		eu = []
		tsp = []

		for j in range (0,len(x)):
			last = j+1
			if last == len(x)-1:
				last = 0
				s = (pow(x[f]-x[j],2) + pow (y[f]-y[j],2)) #N
				eu.append(math.sqrt(s))

			else:
				s = (pow(x[f]-x[j],2) + pow (y[f]-y[j],2)) #N
				eu.append(math.sqrt(s))

		# Sort indices
		_indexSort = np.array(np.argsort(eu))

		# Tour TSP
		indexSort = list(_indexSort)

		for x in range (0,len(indexSort)):
			tsp.append(int(indexSort[x]))

		# Insert
		tsp.insert(len(tsp),f)


		# Last distance
		_lTour = POINTS[tsp[len(tsp)-1]]
		_lTour2 = POINTS[tsp[len(tsp)-2]]
		s = (pow(_lTour[0]-_lTour2[0],2) + pow (_lTour[1]-_lTour2[1],2))
		eu.append(math.sqrt(s))

		# Distance
		distance = sum(eu)

		f += 1

		timeController(tsp,eu)

def timeController(tsp,eu):

	global TOTAL_TIME

	tour = []
	day = 0
	time = 0
	# print(tsp)
	# print(eu)

	for i in range(0,(len(tsp)-1)):

		limit = LIMIT
		j = i+1

		if j == len(tsp)-1:
			j = i


		dst_return = distance.euclidean(POINTS[0],POINTS[i])
		time = time + VISIT_TIME[i] + eu[i]
		
		if time + dst_return < limit and time + dst_return + VISIT_TIME[j] < limit:
			tour.append(tsp[i])


		else:
			tour.insert(len(tour),0)
			totalTime = time - VISIT_TIME[i] - eu[i] + dst_return

			TOTAL_TIME += totalTime

			print('Day '+str(day) + ': ', tour, ' Time:', totalTime)
			del tour[:]
			tour.append(0)
			tour.append(tsp[i])
			day += 1
			time = dst_return + VISIT_TIME[i]

	tour.insert(len(tour),0)
	totalTime = time + VISIT_TIME[i] + dst_return
	print('Day '+str(day) + ': ', tour, ' Time:', totalTime)

	TOTAL_TIME += totalTime

	print('\n')
	print('Total days: ', day)
	print('Total min: ', TOTAL_TIME)






setData()
