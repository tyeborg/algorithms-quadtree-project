import pandas as pd
import ctypes
import pprint

# Create a class that will define the range of the QuadTree
class Rectangle:
    def __init__(self, center, width, height):
        # Define the key properties to acheiving the range
        self.center = center
        self.width = width
        self.height = height
        # Define four more properties: north, south, east, west
        self.west = center.x - width
        self.east = center.x + width
        self.north = center.y - height
        self.south = center.y + height
    
    # Create a method to determine whether a point fits within the Quadtree
    def containsPoint(self, point):
        return (self.west <= point.x < self.east 
                and self.north <= point.y < self.south)