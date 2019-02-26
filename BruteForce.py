import time

# Runs the brute force convex hull algorithm on a set of points and returns the time taken to execute
def ConvexHullBruteForce(points):

    # The idea is to loop through every possible line and determine whether or not all the other points lie on one side of the two planes or not
    # If so, we've found a line that is part of the convex hull

    # Get the starting time
    startingTime = time.time()
    # The array of points of the convex hull
    convexHullPoints = []
    # Loop through each point
    for i in range(0, len(points)):
        # For each point, we need to make a line between this current point an all other points
        for j in range(0, len(points)):
            # Make sure the point we're making a line to is not our own point
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                continue
            # Create the line based off of the equation ax + by = c and check whether or not the equation ax + by - c has the same sign for all points

            # a = y2 - y1
            a = (points[j][1] - points[i][1])
            # b = x2 - x1
            b = (points[j][0] - points[i][0])
            # c = x1 * y2 - y1 * x2
            c = points[i][0] * points[j][1] - points[i][1] * points[j][0]

            # The last value of ax + by - c in the loop below
            lastValue = 0
            # Loop through all the points and check whether or not the ax + by - c has the same sign for all points to determine whether or not this line is part of the convex hull
            for k in range(0, len(points)):
                # If we're on the first element, just set the last value since there's nothing to compare it to
                if k == 0:
                    lastValue = (a * points[k][0]) + (b * points[k][1]) - c
                # If the last value has a different sign then the current value, stop the loop here
                elif lastValue < 0 and ((a * points[k][0]) + (b * points[k][1]) - c) > 0 or lastValue > 0 and ((a * points[k][0]) + (b * points[k][1]) - c) < 0:
                    break
                # If the last value had the same sign as the current value and we're on the last element, these two points must be part of the convex hull
                elif k == len(points) - 1:
                    if not convexHullPoints.__contains__([[points[i][0], points[i][1]]]):
                        convexHullPoints.append([[points[i][0], points[i][1]]])
                    if not convexHullPoints.__contains__([[points[j][0], points[j][1]]]):
                        convexHullPoints.append([[points[j][0], points[j][1]]])
                # If everything's good, just set the last value
                else:
                    lastValue = ((a * points[k][0]) + (b * points[k][1]) - c)

    return time.time() - startingTime
