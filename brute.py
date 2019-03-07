import pgon
import cv2
import numpy as np

data = pgon.gen(6,1)  #generate the data to find a convex hull for
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
			edge.append([data[i],data[j]])
			
			#The code below would coudl replace the edge.append above to generate the specific points that would match quickhull, 
			#but they would be out of order for drawing the lines, so instead i just appended the hull points as above for easy line drawing in the loop below
			#if data[i] not in edge:
			#	edge.append(data[i])
			#if data[j] not in edge:
			#	edge.append(data[j])
				
img = np.zeros([400,400,3])	#make a black image
for i in range(1,len(edge)):	#for each line data draw a line
	 cv2.line(img,edge[i][0],edge[i][1],(255,0,0),1)
	
cv2.imshow('image',img)	#show the image



cv2.waitKey(2000)