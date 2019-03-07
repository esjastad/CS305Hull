from shapely.geometry import Polygon, Point
import random
import math 
from math import pi, cos, sin

#generate points inside the polygon
def genInnerPoints(shaped, num):
	
	poly = Polygon(shaped[0])	#create a polygon using shapely, polygon based on initial shaped data
	min_x, min_y, max_x, max_y = poly.bounds	#get min max of x,y coords

	b = []
	b.append([(199,199)])	#append list with center point, just to get index 0 going
	
	while len(b[0]) < (num-1):	#while we dont have enough points generated
		rp = Point([random.uniform(int(min_x), int(max_x)), random.uniform(int(min_y), int(max_y))])  #attempt gen point in range
		if (rp.within(poly)):	#if generated point is within the polygon add it to the list
			b[0].extend([(int(rp.x),int(rp.y))])

		
	return b
		
#generate a polygon
def gen(n,num):
	xy = []
	if n < 3:	#generate random
		xy.append([(random.randint(0,399),random.randint(0,399)) for i in range (10**num)])
	elif n == 3:	#generate triangle
		xy.append([(49,349),(349,349),(199,49)])
		xy[0].extend(genInnerPoints(xy,((10 ** num) - 3))[0]) 	#populate interior of polygon
		
	elif n == 4:	#generate square
		angles = 360/n
		
		r = 150 #radius from center
		xy = []
		xy.append([(int(199 + r * sin(math.radians(45))),int(199 + r * cos(math.radians(45))))])
		for i in range (1,n):
			p = (int(199 + r * sin(math.radians(angles *i+45))),int(199 + r * cos(math.radians(angles * i+45))))
			xy[0].extend([p])
		
		#populate interior of polygon
		b = genInnerPoints(xy,((10**num)-n))
		if len(b[0]) > 1:
			xy[0].extend(b[0])
			
	else:	#generate n sided polygon
		angles = 360/n
		
		r = 150 #radius from center
		xy = []
		xy.append([(int(199 + r * sin(math.radians(180))),int(199 + r * cos(math.radians(180))))])
		for i in range (1,n):
			p = (int(199 + r * sin(math.radians(angles *i+180))),int(199 + r * cos(math.radians(angles * i+180))))
			xy[0].extend([p])
		
		#populate interior of polygon
		b = genInnerPoints(xy,((10**num)-n))
		if len(b[0]) > 1:
			xy[0].extend(b[0])
	
	return xy

	





