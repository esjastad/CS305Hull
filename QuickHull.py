import cv2
import numpy as np
import random
import copy
import time
import tkinter as tk
import math 
from math import pi, cos, sin
from shapely.geometry import Polygon, Point

#animation flashing point
def Pdraw(points, p1,p2,p3,img,c):
	for i in points:
		img[i[1],i[0]] = (0,255,155)
	cv2.line(img,p1,p2,c,1)
	for i in range (0,4):
		img[p3[1],p3[0]] = (255,255,255)
		cv2.imshow('test', img)		#show the window test with the image img
		cv2.waitKey(500)				#wait for milliseconds specified
		img[p3[1],p3[0]] = (0,0,255)
		cv2.imshow('test', img)		#show the window test with the image img
		cv2.waitKey(500)				#wait for milliseconds specified

#draw circle around selected point
def Cdraw(p, img):
	cv2.circle(img, p, 3, (255,255,255), 1)
	cv2.imshow('test', img)		#show the window test with the image img
	cv2.waitKey(1000)

	
#quicksort
def partition(array, begin, end):
    pivot = begin
    for i in range (begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin, end):   
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)	
	
#For sorting the x values in generated points
def qsort(InputList):
	end = len(InputList)-1
	InputList = quicksort(InputList,0,end)
	

#Generate Top and Bottom hull startHull for NO ANIMATION
def quickhull(points, p1, p2):

	startHull = time.time()
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
		
		#distance from line generate by x1y1 and 2y2
		d = x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3
		if(round(d) > 0):
			bList.append(points[i])
			if(d > bbest):
				bbest = d
				bmax = points[i]

			
		elif(round(d)<0):
			tList.append(points[i])
			if (d < tbest):
				tbest = d
				tmax = points[i]

	
	#Generate bottom hull
	if len(bList) > 1:
		bList.remove(bmax)

		hull = quickb(bList, p1, bmax)	#recursive call to bottom hull left half
		hull = hull + quickb(bList, bmax, p2) #recursive call to bottom hull right half
	elif bmax:	#if no points list then hull is done
		hull.append(p1)
		hull.append(bmax)
	else:	#if no max then hull is done
		hull.append(p1)
	
	#Generate top hull 
	if len(tList) > 1:
		tList.remove(tmax)
		
		hull = hull + quickt(tList, tmax, p2) 	#recursive call to top hull right half
		hull = hull + quickt(tList, p1, tmax)	#recursive call to top hull left half
	elif tmax:
		hull.append(p2)
		hull.append(tmax)
	else:
		hull.append(p2)
	print(time.time() -startHull)	
	return hull

#Generate bottom convex hull for NO ANIMATION	code is nearly identical to quickhull but only generates bottom hull
def quickb(points,p1,p2):
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

	if len(bList) == 1:
		bList.remove(bmax)

	if len(bList) == 0:
		hull.append(p1)
		if bmax:
			hull.append(bmax)
	else:
		hull = hull + quickb(bList, p1,bmax)
		hull = hull + quickb(bList, bmax, p2)
	
	return hull

#Generate top convex hull for NO ANIMATION code is nearly identical to quickhull but only generates top hull
def quickt(points,p1,p2):
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

	
	
	if len(tList) == 1:
		tList.remove(tmax)
		
	if len(tList) == 0:
		hull.append(p2)
		if tmax:
			hull.append(tmax)
	else:
		hull = hull + quickt(tList, tmax,p2)
		hull = hull + quickt(tList, p1, tmax)
		

	return hull	


#Generate Top and Bottom hull startHull for Animation
def aquickhull(points, p1, p2,img):

	bbest = 0	#used to check if farthest point distance for comparison to bottom hull
	tbest = 0	#used to check if farthest point distance for comparison to top hull
	bmax = None #used to store farthest point for bottom hull
	tmax = None #used to store farthest point for top hull
	bList = []	#used to store bottom hull points
	tList = []	#used to store top hull points
	img2 = copy.copy(img)
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

			
		elif(round(d)<0):
			tList.append(points[i])
			if (d < tbest):
				tbest = d
				tmax = points[i]

	
	#Generate bottom hull
	if len(bList) > 1:
		bList.remove(bmax)

		Pdraw(bList,p1,p2,bmax,img2,(0,255,0))
		
		hull = aquickb(bList, p1, bmax,img2)	#recursive call to bottom hull left half
		hull = hull + aquickb(bList, bmax, p2,img2) #recursive call to bottom hull right half
	elif bmax:	#if no points list then hull is done
		hull.append(p1)
		hull.append(bmax)
	else:	#if no max then hull is done
		hull.append(p1)
	
	#Generate top hull 
	if len(tList) > 1:
		tList.remove(tmax)
		
		Pdraw(tList,p1,p2,tmax,img2,(0,255,0))
		
		hull = hull + aquickt(tList, tmax, p2,img2) 	#recursive call to top hull right half
		hull = hull + aquickt(tList, p1, tmax,img2)	#recursive call to top hull left half
	elif tmax:
		hull.append(p2)
		hull.append(tmax)
	else:
		hull.append(p2)

	return hull

#Generate bottom convex hull	code is nearly identical to quickhull but only generates bottom hull
def aquickb(points,p1,p2,img):
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

	if len(bList) == 1:
		bList.remove(bmax)

	if len(bList) == 0:
		cv2.line(img,p1,p2,(255,0,0),1)
		hull.append(p1)
		Cdraw(p1,img)
		if bmax:
			hull.append(bmax)
			Cdraw(bmax,img)
	else:
		Pdraw(bList,p1,p2,bmax,img,(255,0,0))
		hull = hull + aquickb(bList, p1,bmax,img)
		hull = hull + aquickb(bList, bmax, p2,img)
	
	return hull

#Generate top convex hull code is nearly identical to quickhull but only generates top hull
def aquickt(points,p1,p2,img):
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

	
	if len(tList) == 1:
		tList.remove(tmax)
		
	if len(tList) == 0:
		cv2.line(img,p1,p2,(255,0,0),1)
		hull.append(p2)
		Cdraw(p2,img)
		if tmax:
			hull.append(tmax)
			Cdraw(tmax,img)
	else:
		Pdraw(tList,p1,p2,tmax,img,(255,0,0))
		hull = hull + aquickt(tList, tmax,p2,img)
		hull = hull + aquickt(tList, p1, tmax,img)
		

	return hull



















def startHull(points,img,anim):
	if points == None:
		return
		
	if anim == 1:
		hull = aquickhull(points,points[0],points[len(points)-1],img)
		#color hull points red
		for i in hull:
			img[i[1],i[0]] = (0,0,255)
			
		cv2.imshow('test', img)		#show the window test with the image img
		cv2.waitKey(500)
		
		#connect the dots with lines for the hull
		for i in range(0,len(hull)-1):
			cv2.line(img,hull[i],hull[i+1],(0,255,0),1)
			cv2.imshow('test', img)		#show the window test with the image img
			cv2.waitKey(500)
			
		cv2.line(img,hull[len(hull) -1],hull[0],(0,255,0),1)	#connect the last line	
		cv2.imshow('test', img)		#show the window test with the image img
	else:
		#generate quickhull feeding in sorted extremes as startHulling point
		hull = quickhull(points,points[0],points[len(points)-1])
	
		
	


class gui(tk.Tk):
	points = None
	img = None
	def __init__(self):
			
		tk.Tk.__init__(self)
		self.title("Convex Hull")	# title of gui 
	
		#Code for number of points input in GUI		
		self.label = tk.Label(self, text = "Polygon with n side/points").pack()	
		sv2 = tk.StringVar()	#variable for text field n point polygon
		sv2.trace("w", lambda name, index, mode, sv2=sv2: self.onselect(self))	#call onselect when field edited
		vcmd2 = (self.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.e = tk.Entry(self, validate = 'key', validatecommand = vcmd2, textvariable = sv2) #entry field using var and validation
		self.e.insert(0,'3')  # set def value to 3 in entry field
		self.e.pack()
		self.label3 = tk.Label(self, text = "n values less than 3 = random shape").pack()		
		
		#code for animate check button
		self.var = tk.IntVar()
		self.check = tk.Checkbutton(self, text="Animate", variable = self.var)
		self.check.pack()
		
		#Code for number of points input in GUI		
		self.label2 = tk.Label(self, text = "Number of points to the power of 10").pack()
			
		sv = tk.StringVar()
		sv.trace("w", lambda name, index, mode, sv=sv: self.onselect(self))
		vcmd = (self.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.datap = tk.Entry(self, validate = 'key', validatecommand = vcmd, textvariable = sv)
		self.datap.insert(0,'2')
		self.datap.pack()
		
		#Run button
		self.button = tk.Button(self, text="Run", command = self.go).pack()

	#Check if text entered is the values below, if so return true and print character in field
	def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
		if text in '0123456789':
			return True
		else:
			return False
			
	def go(self):	#when run it pressed check that settings were valid and run
		try:
			sides = int(self.e.get())
			anim = self.var.get()
			numpoints = int(self.datap.get())
			startHull(self.points,self.img,anim)

		except:
			print("Check for Valid Selections!")
				
	def onselect(self,t):	#when data is changed in entry fields generate the respective data
		try:
			sides = int(self.e.get())
			numpoints = int(self.datap.get())
			self.points, self.img = genData(sides,numpoints)
		except:
			return

#wrapper to generate points			
def genpo(sides,num):
	xy = []			
	xy = pgon(sides,(num))
	return xy

#generate points inside the polygon
def genInnerPoints(shaped, num):
	
	poly = Polygon(shaped[0])
	min_x, min_y, max_x, max_y = poly.bounds

	b = []
	b.append([(99,99)])
	
	while len(b[0]) < num:
		rp = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
		if (rp.within(poly)):
			b[0].extend([(int(rp.x),int(rp.y))])
			
	return b
		
#generate a polygon
def pgon(n,num):
	xy = []
	if n < 3:
		xy.append([(random.randint(0,199),random.randint(0,199)) for i in range (10**num)])
	elif n == 3:
		xy.append([(24,174),(174,174),(99,24)])
		xy[0].extend(genInnerPoints(xy,((10 ** num) - 3))[0])
		
	elif n == 4:
		angles = 360/n
		
		r = 75
		xy = []
		xy.append([(int(99 + 75 * sin(math.radians(45))),int(99 + 75 * cos(math.radians(45))))])
		for i in range (1,n):
			p = (int(99 + 75 * sin(math.radians(angles *i+45))),int(99 + 75 * cos(math.radians(angles * i+45))))
			xy[0].extend([p])
	
		xy[0].extend(genInnerPoints(xy,((10**num)-n))[0])
			
	else:
		angles = 360/n
		
		r = 75
		xy = []
		xy.append([(int(99 + 75 * sin(math.radians(180))),int(99 + 75 * cos(math.radians(180))))])
		for i in range (1,n):
			p = (int(99 + 75 * sin(math.radians(angles *i+180))),int(99 + 75 * cos(math.radians(angles * i+180))))
			xy[0].extend([p])
		
		xy[0].extend(genInnerPoints(xy,((10**num)-n))[0])
	
	return xy

#generate all data needed to run
def genData(sides, num):
	if num < 6 and sides <= 360:
		#Generate random points
		data = genpo(sides,num)
		
		#sort the random points
		qsort(data[0])
		
		#generate a 200 by 200 pixel image matrix with 3 values for color
		img = np.zeros([200,200,3])

		data.append(img)
	
	
		#color points green
		for i in data[0]:
			img[i[1],i[0]] = (0,255,0)
		
		img = cv2.resize(img, (400,400))
		cv2.namedWindow('test', 0)	#make a window named test
		cv2.imshow('test', img)		#show the window test with the image img
	elif n < 6 and sides > 360:
		data = genpo(360,num)
		
		#sort the random points
		qsort(data[0])
		
		#generate a 200 by 200 pixel image matrix with 3 values for color
		img = np.zeros([200,200,3])

		data.append(img)
	
	
		#color points green
		for i in data[0]:
			img[i[1],i[0]] = (0,255,0)
		
		img = cv2.resize(img, (400,400))
		cv2.namedWindow('test', 0)	#make a window named test
		cv2.imshow('test', img)		#show the window test with the image img
	else:
		cv2.namedWindow('test', 0)	#make a window named test
		cv2.imshow('test', img)		#show the window test with the image img
		data = None
	img = cv2.resize(img, (400,400))
	return data
	


#main for testing quickhull
if __name__ == "__main__":
	t = gui()
	t.mainloop()
	
	

	
	





