import pandas as pd
import ctypes
import pprint
from point import TupleT
from rectangle import Rectangle

# Create a class that will construct the QuadTree
class QuadTree:
    # For initialization, QuadTree's are defined by their capacity & their boundary.
    def __init__(self, boundary, capacity = 4):
        # Set the properties and their values
        self.boundary = boundary
        self.capacity = capacity
        # Create a variable to store all the given points
        self.points = []
        # Declare a boolean variable as an indicator for...
        # when the QuadTree has been divided or not.
        self.divided = False
        
    # Create a function for inserting all of the points into the QuadTree    
    def insert(self, point):
        # Return false if the point is not within range of the QuadTree.
        if not self.boundary.containsPoint(point):
            return False
        
        # Determine if the quadrant has exceeded capacity.
        if len(self.points) < self.capacity:
            # Add the tuple into the list
            self.points.append(point)
            return True
        
        # At this point, the QuadTree must divide itself.
        if not self.divided:
            self.divide()
            
        # Insert the point to any of the four subtrees...
        # (northwest, northeast, southwest, southeast)
        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True
        
        # No point should ever make it to this return case...
        return False
    
    # Create a function to divide quadrant(s) into multiple quadrants.
    def divide(self):
        # Determine the values for defining the QuadTree.
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2
        
        # Initialize each rectangle for each sub-quadtree.
        # Determine the location of northwest within the quadrant.
        nw = Rectangle(TupleT(center_x - new_width, center_y - new_height, None, None),
                       new_width, new_height)
        self.nw = QuadTree(nw)
        
        # Determine the location of northeast within the quadrant.
        ne = Rectangle(TupleT(center_x + new_width, center_y - new_height, None, None),
                       new_width, new_height)
        self.ne = QuadTree(ne)
        
        # Determine the location of southwest within the quadrant.
        sw = Rectangle(TupleT(center_x - new_width, center_y + new_height, None, None),
                       new_width, new_height)
        self.sw = QuadTree(sw)
        
        # Determine the location of southeast within the quadrant.
        se = Rectangle(TupleT(center_x + new_width, center_y + new_height, None, None),
                       new_width, new_height)
        self.se = QuadTree(se)
        
        # Ensure that the QuadTree has been divided.
        self.divided = True
        
    # Create a search functiion for finding a specific point within the QuadTree.
    def search(self, coordx, coordy, list):
        # Iterate through the points list.
        for p in self.points:
            # Determine if input x and input y equates to tuple x and y.
            if p.x == coordx and p.y == coordy:
                # Add the retailer and postcode of the 
                # chosen tuple into the list
                list.append(p.retailer)
                list.append(p.postcode)
                
        # If not in the initial list, recursively search throughout each sub-quadtree.
        if self.divided:
            self.nw.search(coordx, coordy, list)
            self.ne.search(coordx, coordy, list)
            self.sw.search(coordx, coordy, list)
            self.se.search(coordx, coordy, list)
        
        # Return the list...
        return list