import data
import datetime


#main for testing quickhull
if __name__ == "__main__":
	shapes = ('Random','Triangle','Square','Decagon','180 Sided Polgygon','Circle')
	nside = (2,3,4,10,180,360)
	currentDT = datetime.datetime.now()
	print (str(currentDT))	
	file = open("ConvexHullData.txt","w")
	
	print("\nStarting data collection\n")
	for i in range (6):	#loop for each shapes
		print("Shape ", shapes[i])
		file.write(shapes[i])
		file.write("\nPoints\tQuick Unsorted Time\tBrute Unsorted Time\tQuick Sorted Time\tBrute Sorted Time\n")	
		
		data.collect(nside,i,file)
	currentDT = datetime.datetime.now()
	print (str(currentDT))	

	





