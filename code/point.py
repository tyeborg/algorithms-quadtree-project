import pandas as pd
import ctypes
import pprint 

# Create a class that will define a point on the QuadTree
class TupleT:
    # Create four properties: x, y, retailer and postcode
    def __init__(self, x, y, retailer, postcode):
        # Set each variable to their respective value
        self.x = x
        self.y = y
        self.retailer = retailer
        self.postcode = postcode