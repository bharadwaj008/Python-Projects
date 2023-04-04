'''Ram shifted to a new place recently. There are multiple schools near his locality. 

Given the co-ordinates of Ram P(X,Y) and schools near his locality in a nested list, find the closest school.

Print multiple coordinates in respective order if there exists multiple schools closest to him. 
 
Write a function closestSchool that accepts (X ,Y , L) where X and Y are co-ordinates of Ram's house and 
 
L contains co-ordinates of different school.

Distance Formula(To calculate distance between two co-ordinates): √((X2 - X1)² + (Y2 - Y1)²)

where (x1,y1) is the co-ordinate of point 1 and (x2, y2) is the co-ordinate of point 2.
Input:
X, Y (Ram's house co-ordinates)
N (No of schools)
X1 Y1
X2 Y2
.
.
.

X6 Y6

Output:
Closest pont/points to X, Y
'''



'''so here basically we will be given one point assume it's our co-ordinate and we will be given some number of
other co-ordinates and we should find the nearest points and print them '''

from math import sqrt
#from math import dist

#defining our function
def closestSchool(x,y,L):
    #creating list for saving distance of every point to our point
    dist_lst = []
    #creating point(tuple) which is our point to calculate distance fromm every point. 
    p= x,y

    #looping in the list of points that were given to calculate euclidean distance between 2 points. 
    for q in L:
        dist = sqrt(sum((px-qx)**2.0 for px,qx in zip(p,q)))
    #instead we an also use dist(p,q) function from math module whicch calulates euclidean distance(available in >=v3.8)
        dist_lst.append(dist)
        #appending the dist of eah point in this list.
        
    min1 = min(dist_lst)
    #calculating the minimum distance using min() function in dist_lst
   
    out = [ele for ele,ele1 in zip(L,dist_lst) if ele1 == min1]
    #creating list of points that were at minimum distance from our point using parallel looping of 2 lists
    #using zip() function.

    #alternatively, u can use a dictionary to do this instead of two lists, some memory will be saved.

    print(*out,sep='\n')
    #printing the points that were at minimum distance with seperator '\n'


x, y = map(int, input().split())
#taking input of our point

n = int(input())
#number of points to take input for calculating distance
L = []
#created list for appending the points to calculate distance
for i in range(n):
    #as the input of each point is in same line we r using map function to map int to convert string to integer. 
    l = list(map(int, input().split()))
    L.append(l)

#calling the function defined by us to print the closest points.
closestSchool(x, y, L)