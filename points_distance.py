#!/usr/bin/python
# Also a demo of OOP in Python

class Point():
    """Location of a point in 2-D space"""

def distance_between_points(p1, p2):
    import math
    dist = math.sqrt( (p2.x - p1.x)**2 + (p2.y - p1.y)**2 )
    return dist

# Create instance (object) of Point class
p1 = Point()
p2 = Point()

# Set instance attributes
p1.x = 2
p1.y = 3
p2.x = 5
p2.y = 4

print distance_between_points(p1, p2)
