import time

#Quickhull without sorted data
def sorted(points, p1, p2, loop):

	startHull = time.time() #get starting time for performance
	hull = []
	if loop == 1:
		for i in range (100):
		
			bbest = 0	#used to check if farthest point distance for comparison to bottom hull
			tbest = 0	#used to check if farthest point distance for comparison to top hull
			bmax = None #used to store farthest point for bottom hull
			tmax = None #used to store farthest point for top hull
			bList = []	#used to store bottom hull points
			tList = []	#used to store top hull points
			
			x1, y1 = p1 #cartesian coords
			x2, y2 = p2
			
			hull = []	#hull coords list 	
			#if no loop is needed on a small data set run this
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
			
		b = (time.time() - startHull)/100

	else:
		
		bbest = 0	#used to check if farthest point distance for comparison to bottom hull
		tbest = 0	#used to check if farthest point distance for comparison to top hull
		bmax = None #used to store farthest point for bottom hull
		tmax = None #used to store farthest point for top hull
		bList = []	#used to store bottom hull points
		tList = []	#used to store top hull points
		
		x1, y1 = p1 #cartesian coords
		x2, y2 = p2
		
		hull = []	#hull coords list 	
		#if no loop is needed on a small data set run this
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
		
		b = time.time() - startHull

	return b

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

#Quickhull with sorted data
def unsorted(points, p1, p2, loop):

	startHull = time.time() #get starting time for performance

	if loop == 1:
		for i in range (100):
			p1 = points[0]
			p2 = points[0]
			for i in points:
				if i[0] > p2[0]:
					p2 = i
				elif i[0] < p1[0]:
					p1 = i
			bbest = 0	#used to check if farthest point distance for comparison to bottom hull
			tbest = 0	#used to check if farthest point distance for comparison to top hull
			bmax = None #used to store farthest point for bottom hull
			tmax = None #used to store farthest point for top hull
			bList = []	#used to store bottom hull points
			tList = []	#used to store top hull points
			
			x1, y1 = p1 #cartesian coords
			x2, y2 = p2
			
			hull = []	#hull coords list 	
			#if no loop is needed on a small data set run this
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
			
		b = (time.time() - startHull)/100
		
	else:
		p1 = points[0]
		p2 = points[0]
		for i in points:
			if i[0] > p2[0]:
				p2 = i
			elif i[0] < p1[0]:
				p1 = i
				
		bbest = 0	#used to check if farthest point distance for comparison to bottom hull
		tbest = 0	#used to check if farthest point distance for comparison to top hull
		bmax = None #used to store farthest point for bottom hull
		tmax = None #used to store farthest point for top hull
		bList = []	#used to store bottom hull points
		tList = []	#used to store top hull points
		
		x1, y1 = p1 #cartesian coords
		x2, y2 = p2
		
		hull = []	#hull coords list 	
		#if no loop is needed on a small data set run this
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
		
		b = time.time() - startHull

	return b
	

	
	
	





