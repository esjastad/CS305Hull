import time
import pgon
import qhull
import qsort


def collect(nside,i,file):
	
	#For 10^1 and 10^2 number of points call the quickhull function feeding in a 1 as the third argument, this causes the quickhull to run 100x and divide the time by 100, otherwise the timing would be 0
	for j in range (1,3):	
		print("10^",j)
		bestTime = 100	
		datap = pgon.gen(nside[i],j)	#Generate datapoints 
		
		for k in range (20):	#Run the algorithm on UNSORTED data 20 times and take the best time result for data collection
			timeResult = qhull.unsorted(datap[0],datap[0][2],datap[0][1],1)
			if timeResult < bestTime:
				bestTime = timeResult
		
		#Save the data to file
		file.write("10^")
		file.write(str(j))
		file.write("\t")
		file.write(str(bestTime))
		file.write("\t")
		
		qsort.sort(datap[0])	#sort the data points
		bestTime = 100
		for k in range (20):	#Run the algorithm on SORTED data 20 times and take the best time result for data collection
			timeResult = qhull.sorted(datap[0],datap[0][2],datap[0][1],1)
			if timeResult < bestTime:
				bestTime = timeResult
		
		#Save the data to file
		file.write(str(bestTime))
		file.write("\t")
		file.write("\n")
	
	#For 10^3 to 10^5 number of points call the quickhull function feeding in a 0 as the third argument, the number of data points is sufficiently long to not need a loop for timing
	for j in range (3,6):	
		print("10^",j)
		bestTime = 100	
		datap = pgon.gen(nside[i],j)	#Generate datapoints 
		
		for k in range (20):	#Run the algorithm on UNSORTED data 20 times and take the best time result for data collection
			timeResult = qhull.unsorted(datap[0],datap[0][2],datap[0][1],0)
			if timeResult < bestTime:
				bestTime = timeResult
		
		#Save the data to file
		file.write("10^")
		file.write(str(j))
		file.write("\t")
		file.write(str(bestTime))
		file.write("\t")
		
		qsort.sort(datap[0])	#sort the data points
		bestTime = 100
		for k in range (20):	#Run the algorithm on SORTED data 20 times and take the best time result for data collection
			timeResult = qhull.sorted(datap[0],datap[0][2],datap[0][1],1)
			if timeResult < bestTime:
				bestTime = timeResult
		
		#Save the data to file
		file.write(str(bestTime))
		file.write("\t")
		
		file.write("\n")	
	
	