import cv2
import numpy as np
import random


#For sorting the x values in generated points
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		# Compare the current element with next one		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

#Generate Top and Bottom hull start
def quickhull(points, p1, p2,img):
	bbest = 0	#used to check if farthest point distance for comparison to bottom hull
	tbest = 0	#used to check if farthest point distance for comparison to top hull
	bmax = None #used to store farthest point for bottom hull
	tmax = None #used to store farthest point for top hull
	bList = []	#used to store bottom hull points
	tList = []	#used to store top hull points

	x1, y1 = p1 #cartesian coords
	x2, y2 = p2
	hull = []	#hull coords
	
	#check each points distance from the "line" between x min and x max
	#build top and bottom hull list as well as the max point for top and bottom
	for i in range (1,len(points)-1):
	
		x3,y3 = points[i]
		
		d = x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3
		if(round(d) > 0):
			bList.append(points[i])
			if(d > bbest):
				bbest = d
				bmax = points[i]
			elif(d == bbest):
				print("Implement ==")
			
		elif(round(d)<0):
			tList.append(points[i])
			if (d < tbest):
				tbest = d
				tmax = points[i]
			elif(d == tbest):
				print("Implement ==")
	
	#Generate bottom hull
	if len(bList) > 1:
		bList.remove(bmax)
		hull = quickb(bList, p1, bmax,img)	#recursive call to bottom hull left half
		hull = hull + quickb(bList, bmax, p2,img) #recursive call to bottom hull right half
	elif bmax:	#if no points list then hull is done
		hull.append(p1)
		hull.append(bmax)
	else:	#if no max then hull is done
		hull.append(p1)
	
	#Generate top hull 
	if len(tList) > 1:
		tList.remove(tmax)
		hull = hull + quickt(tList, tmax, p2,img) 	#recursive call to top hull right half
		hull = hull + quickt(tList, p1, tmax,img)	#recursive call to top hull left half
	elif tmax:
		hull.append(p2)
		hull.append(tmax)
	else:
		hull.append(p2)
			
	return hull

#Generate bottom convex hull	code is nearly identical to quickhull but only generates bottom hull
def quickb(points,p1,p2,img):
	bbest = 0
	bmax = None
	bList = []

	x1, y1 = p1
	x2, y2 = p2
	hull = []
	
	for i in range (0,len(points)):
	
		x3,y3 = points[i]

		d = x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3
		
		if(round(d) > 0):
			bList.append(points[i])
			if(d > bbest):
				bbest = d
				bmax = points[i]
			elif(d == bbest):
				print("Implement ==")
	if len(bList) == 1:
		bList.remove(bmax)
		
	if len(bList) == 0:
		hull.append(p1)
		if bmax:
			hull.append(bmax)
	else:
		hull = hull + quickb(bList, p1,bmax,img)
		hull = hull + quickb(bList, bmax, p2,img)
	
	return hull

#Generate top convex hull code is nearly identical to quickhull but only generates top hull
def quickt(points,p1,p2,img):
	tbest = 0
	tmax = None
	tList = []

	x1, y1 = p1
	x2, y2 = p2
	hull = []
	

	
	for i in range (0,len(points)):
	
		x3,y3 = points[i]
	
		d = x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3
		if(round(d) < 0):
			tList.append(points[i])
			if (d < tbest):
				tbest = d
				tmax = points[i]
			elif(d == tbest):
				print("Implement ==")
	
	
	if len(tList) == 1:
		tList.remove(tmax)
		
	if len(tList) == 0:
		hull.append(p2)
		if tmax:
			hull.append(tmax)
	else:
		hull = hull + quickt(tList, tmax,p2,img)
		hull = hull + quickt(tList, p1, tmax,img)
		

	return hull	


#main for testing quickhull
if __name__ == "__main__":	
	#Generate random points
	points = [(random.randint(1,199), random.randint(1,199)) for k in range(10)]
	#sort the random points
	insertion_sort(points)



	#generate a 200 by 200 pixel image matrix with 3 values for color
	img = np.zeros([200,200,3])


	#generate quickhull feeding in sorted extremes as starting points
	hull = quickhull(points,points[0],points[len(points)-1],img)

	#connect the dots with lines for the hull
	for i in range(0,len(hull)-1):
		cv2.line(img,hull[i],hull[i+1],(0,255,0),1)
	cv2.line(img,hull[len(hull) -1],hull[0],(0,255,0),1)	#connect the last line

	#color internal points blue
	for i in points:
		img[i[1],i[0]] = (255,0,0)

	#color hull points red
	for i in hull:
		img[i[1],i[0]] = (0,0,255)

	cv2.namedWindow('test', 0)	#make a window named test
	cv2.imshow('test', img)		#show the window test with the image img
	
	cv2.waitKey(0)				#wait forever until a key is pressed
	cv2.destroyAllWindows()		#close window





