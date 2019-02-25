# k-means clustering
# author: Matt Drew
# desctription: learn.py implements k-means clustering. This program in particular implements for k=2.
import random

# GLOBAL VARIABLES
# data points to cluster
data = [[1,7],[1,11],[3,17],[7,18],[8,4],[8,12],[11,7],[12,14],[13,17],[16,11]]
dataCentroid1 = []
dataCentroid2 = []
oldDataCentroid1 = []
oldDataCentroid2 = []
centroid1 = []
centroid2 = []
iteration = 1

# how many clusters are there?
k = 2

#################################################

def dist_func(centroidList, dataPoint):
    # do distance function here...
    centroidPoint1 = centroidList[0]
    centroidPoint2 = centroidList[1]
    # manhattan distance = | xi1 - xj1 | + |xi2 - xj2|
    distanceCentroid1 = abs(dataPoint[0] - centroidPoint1[0]) + abs(dataPoint[1] - centroidPoint1[1])
    distanceCentroid2 = abs(dataPoint[0] - centroidPoint2[0]) + abs(dataPoint[1] - centroidPoint2[1])
    if(distanceCentroid1 > distanceCentroid2):
        return centroidPoint2
    else:
        return centroidPoint1

def get_init_centroid():
    # get k # of random centroids to start with
    randOld = -1
    centroid = []
    for i in range(0,k):
        rand = random.randint(0,9)
        # make sure that there's no duplicate centroid!
        if(rand == randOld):
            print("it's the same!")
            while(rand == randOld):
                rand = random.randint(0,9)
                print("rand: " , rand)
                print("randOld: " , randOld)
                randOld == rand
        centroid.append([data[rand][0], data[rand][1]])
        randOld = rand
    return centroid

def calc_new_centroid(centroid, data):
    # initialize data
    n = len(data)
    x_values = 0
    y_values = 0

    # sum the x and y values in the datapoints.
    for i in range(0,len(data)):
        x_values = x_values + data[i][0]
        y_values = y_values + data[i][1]

    # calculate the new x value with 1 decimal place.
    new_x_value = round(x_values * (1/n), 1)
    new_y_value = round(y_values * (1/n), 1)

    # return the mean x value and mean y value
    return [new_x_value, new_y_value]

# get initial random centroids
centroids = get_init_centroid()
print("initial centroids: " , centroids)

# store them as global variables
centroid1 = centroids[0]
centroid2 = centroids[1]

while(1):
    print("============ ITERATION " + str(iteration) + " START ===============")

    # iterate through the data and assign all the datapoints a closest centroid
    for i in range(0, len(data)):
        dataPoint = [data[i][0], data[i][1]]
        closestCentroid = dist_func(centroids, dataPoint)
        # assign the datapoint a centroid
        if(closestCentroid == centroid1):
            dataCentroid1.append(dataPoint)
        else:
            dataCentroid2.append(dataPoint)

    # keep centroid history
    oldCentroid1 = centroid1
    oldCentroid2 = centroid2

    # calculate new centroid based on new clusters
    centroid1 = calc_new_centroid(centroid1, dataCentroid1)
    centroid2 = calc_new_centroid(centroid2, dataCentroid2)
    centroids = [centroid1, centroid2]

    print("dataCentroid1: ", dataCentroid1)
    print("dataCentroid2: ", dataCentroid2)
    print("\n")
    print("new centroid1: ", centroid1 , " | old centroid1: " , oldCentroid1)
    print("new centroid2: ", centroid2 , " | old centroid2: " , oldCentroid2)

    # stoppage criteria
    if((centroid1 == oldCentroid1) & (centroid2 == oldCentroid2)):
        print("centroids are the same. cluster complete.")
        break
    # if the data points are the same as the last iteration's datapoints
    if((dataCentroid1 == oldDataCentroid1) & (dataCentroid2 == oldDataCentroid2)):
        print("data clusters have not changed from last iteration. cluster complete.")
        break

    # save and clear the centroid-assigned datapoints to get ready for the next iteration.
    oldDataCentroid1 = dataCentroid1
    oldDataCentroid2 = dataCentroid2
    dataCentroid1 = []
    dataCentroid2 = []

    # up the iteration count
    iteration = iteration + 1

    print("=========== ITERATION END ============\n")
