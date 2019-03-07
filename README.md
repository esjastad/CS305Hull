# CS350Hull
ConvexHull Algorithm Comparisons

Data points for ConvexHull generation is a tuple in the cartesian plane, (x,y coordinate)
The quikchull algorithm uses the minimum and maximum X valued data points as a starting point.

If the data is sorted already then quickhull can use the first and last data points, Otherwise Quickhull as to do a O(n) search through the points to find the min and max first.

The quickhull algorithm starts by iterating across each point in the data set and calculating their distance from the line between the min/max points we started with.  If a data points distance is negative it is added to a list for generating the bottom hull, if the data points distance is positive it is added to a list for generating the top hull.    

The positive points list and its farthest positive point are then recusrively passed into a function to generate the top hull.  This function has to be called twice:
            Once using Min x and the farthest positive point,  Passing in the positive point list to iterate across
            Once Using Max x and the farthest positive point,  Passing in the positive point list to iterate across
            
Each time the number of points in each list is being reduced by a variable amount,  on average the number of points is being halved.

The function that is called to generate the top hull will now iterate across the points and find the furthest one and generate a positive point list ONLY! it does not care about negative points anymore because they are inside the hull.  This happens recursively until there are no points left in the list to iterate across.  

Each max distance point found is added to the list of points that make the convex hull (this includes the starting x min and x max)

The same exact process occurs for the bottom hull/negative point list as well.

The final returned hull points list contains the points IN ORDER to draw lines for a convex hull.


The iterations give a performance of O(n) and the recursive call is O(log n)  yielding a performance of O(n log n)


# data collection

The data is collected by generating random points, triangle, square, Decagon, 180 sided, and circle 360 sided polygon
For each shape type we generate unsorted data with a total number of points 10^1 to 10^5.

Each shape and 10^n is ran through quickhull generation 20 times and the best time is kept and written to file.
After the time is calculated for UNSORTED we then take the SAME data and sort it and run the algoirithm again in the same fashion 20x and keep the best time.     (brute force will also use the same data set quickhull used for sorted and unsorted once it is ready)

If the number of points is too small, 10^1 and 10^2 the quickhull algorithm is looped 100x and the capture time is divided by 100 otherwise the time result is 0.

The data file created is a .txt file where each data field is seperated by a tab, This is great because you can go into excel or google spreadsheets and import the .txt and each block will be populated accordingly for easy graphing or data analysis.

# Interesting things
Quickhull timing seems to be influenced by the number of points to iterate across as well as the shape.  So a square is faster than a circle for quickhull because for a square only finds 2 other distant points and so only runs recursively 2x but a cricle with 360 points will typically have to recur 60x or more (its not 360 because some of those points lie on the line and have a distance of 0)

Another interesting issue I have found in the data is that the sorted data seems to take longer than unsorted for quickhull.  I can not think of a reason why this is happening, but I feel like we need to discover why.   This makes no sense to me because the unsorted algorithm has the additional time overhead of iterating across the points first to find the min and max, while the sorted call does not do this!  THE ALGORITHMS ARE THE SAME!!! it was a simple copy paste and the only difference is adding the loop to find the min max, you can see this code in qhull.py    line 4 is where the sorted alg starts and line 200 is where the unsorted alg starts.   The only difference is the addition of line 206 to 212 which is where the points are iterated across to find the min/max.  (274 to 280 is the same addition as 206 to 212, this is because of the if else for wethere we should loop 100x or not).


It currently takes around 30-45 minutes to generate the data just for quickhull.  If we added the 10^6 data collection the process would probably take 2+ hours just for quickhull, this is because it is already doing 6 shapes and 5 powers of data points.  so 30 different runs that happen 20x each making it a total of 600 runs, but this is just for sorted data, then unsorted does another 600 making 1,200 runs total.  Each higher power for 10^n takes longer as well since the algorithm is n logn.

If we would like to use more than 10^5 data points, change line 40 in data.py.  Change the 6 in the for loop to 7 to include 10^6, to 8 to include 10^7 and so on.
