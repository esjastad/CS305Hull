import pgon


data = pgon.gen(4,1)  #generate the data to find a convex hull for
data = data[0]
edge = []
size = len(data)

for i in range (size):
	for j in range (size):
		if j == i:
			continue
		direction = 0	#set to 0, used to determine if all points should be pos or neg
		flag = 0
		for k in range (size):	
			if k == j or k == i:
				continue
			
			#x1, y1 = data[i]#cartesian coords
			#x2, y2 = data[j]
			#x3, y3 = data[k]
			#side = x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3
			#side below is the same as the commented code above 
			side = data[i][0]*data[j][1]+data[k][0]*data[i][1]+data[j][0]*data[k][1]-data[k][0]*data[j][1]-data[j][0]*data[i][1]-data[i][0]*data[k][1]
			
			if side < 0: 
				if direction == 0:  #if direction is not set yet then set it
					direction = -1
				elif direction > 0:  #if direction is a mismatch then break out of loop because i,j can not be convex hull
					flag =1		# set this flag to break out of j loop
					break
			elif side > 0:
				if direction == 0:	#if direction is not set yet then set it
					direction = 1
				elif direction < 0:	#if direction is a mismatch then break out of loop because i,j can not be convex hull  
					flag = 1	# set this flag to break out of the j loop
					break
		if flag != 1:	# if not part of convex hull break out to iterate i						
			if data[i] not in edge:
				edge.append(data[i])
			if data[j] not in edge:
				edge.append(data[j])
				

#the data for the convex hull points isnt in a perfect order but they are all there
#I have also tried manually setting the data to make sure it still captures all the points 
#even if it is scrambled instead of being at the front of the list
print(data)
print(edge)
	
	

