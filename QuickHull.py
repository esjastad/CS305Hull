import cv2
import numpy as np
import random
import copy
import time
import tkinter as tk

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

def Cdraw(p, img):
	cv2.circle(img, p, 3, (255,255,255), 1)
	cv2.imshow('test', img)		#show the window test with the image img
	cv2.waitKey(1000)

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
	start = time.time()
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

		#Pdraw(bList,p1,p2,bmax,img2,(0,255,0))
		
		hull = quickb(bList, p1, bmax,img2)	#recursive call to bottom hull left half
		hull = hull + quickb(bList, bmax, p2,img2) #recursive call to bottom hull right half
	elif bmax:	#if no points list then hull is done
		hull.append(p1)
		hull.append(bmax)
	else:	#if no max then hull is done
		hull.append(p1)
	
	#Generate top hull 
	if len(tList) > 1:
		tList.remove(tmax)
		
		#Pdraw(tList,p1,p2,tmax,img2,(0,255,0))
		
		hull = hull + quickt(tList, tmax, p2,img2) 	#recursive call to top hull right half
		hull = hull + quickt(tList, p1, tmax,img2)	#recursive call to top hull left half
	elif tmax:
		hull.append(p2)
		hull.append(tmax)
	else:
		hull.append(p2)
	print(time.time() -start)	
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
		#cv2.line(img,p1,p2,(255,0,0),1)
		hull.append(p1)
		#Cdraw(p1,img)
		if bmax:
			hull.append(bmax)
			#Cdraw(bmax,img)
	else:
		#Pdraw(bList,p1,p2,bmax,img,(255,0,0))
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
		#cv2.line(img,p1,p2,(255,0,0),1)
		hull.append(p2)
		#Cdraw(p2,img)
		if tmax:
			hull.append(tmax)
			#Cdraw(tmax,img)
	else:
		#Pdraw(tList,p1,p2,tmax,img,(255,0,0))
		hull = hull + quickt(tList, tmax,p2,img)
		hull = hull + quickt(tList, p1, tmax,img)
		

	return hull	

def start():

	val = int(t.list.curselection())
	print(val)

	
	#Generate random points
	n = 2
	points = [(random.randint(1,199), random.randint(1,199)) for k in range(10 ** n)]
	#sort the random points
	insertion_sort(points)

	cv2.namedWindow('test', 0)	#make a window named test

	#generate a 200 by 200 pixel image matrix with 3 values for color
	img = np.zeros([200,200,3])
	
	#color points green
	for i in points:
		img[i[1],i[0]] = (0,255,0)
	
	cv2.imshow('test', img)		#show the window test with the image img
	cv2.waitKey(1000)
	
	#generate quickhull feeding in sorted extremes as starting points
	hull = quickhull(points,points[0],points[len(points)-1],img)
	

	cv2.namedWindow('test', 0)	#make a window named test
	
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
	
	cv2.waitKey(0)				#wait forever until a key is pressed
	cv2.destroyAllWindows()		#close window


class gui(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Convex Hull")
		self.lable = tk.Label(self, text = "Select Data Point Shape").pack()
		
		choices = ['Star','Triangle','Circle','Square','Random']
		self.list = tk.Listbox(self, height = 5)
		for i in choices:
			self.list.insert(0,i)
		self.list.select_set(0) #This only sets focus on the first item.
		self.list.pack()
		
		
		self.check = tk.Checkbutton(self, text="Animate")
		self.check.pack()
		self.lable2 = tk.Label(self, text = "Number of points to the power of 10").pack()
		
		
		vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')		
		self.datap = tk.Entry(self, validate = 'key', validatecommand = vcmd)
		self.datap.insert(0,'1')
		self.datap.pack()
		self.button = tk.Button(self, text="Run", command = self.go).pack()
	
	def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
		if text in '0123456789*-+':
			try:
				int(value_if_allowed)
				return True
			except ValueError:
				return False
		else:
			return False
			
	def go(self):
		selection = int(self.list.curselection()[0])
		numpoints = int(self.datap.get())
		anim = self.check.state()
		print(anim)
	
#main for testing quickhull
if __name__ == "__main__":
	t = gui()
	t.mainloop()
	
	

	
	





