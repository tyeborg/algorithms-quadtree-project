import pandas as pd
import ctypes
import pprint
from point import TupleT
from rectangle import Rectangle
from quadtree import QuadTree
from hashtable import ST

# Create a function that returns the read data of csv file
def read_data():
    # Utilize try and except to account for incorrect file paths, etc.
    try:
        df = pd.read_csv("uk_glx_open_retail_points_v20_202104.csv")
        return df
    except FileNotFoundError:
        # Notify the user of the file not existing within your current path.
        print("'uk_glx_open_retail_points_v20_202104.csv' does not exist within your Path.")

# Create a function for receiving and validating longitude input.
def get_x():
    
    # Declare boolean variable for validation purposes.
    invalid = True
    
    while invalid == True:
        try:
            x = float(input("\nPlease enter longitude: "))
            print("'{}' has been accepted...".format(x))
            # Exit the while loop.
            invalid = False
        # Call upon a value error, if input cannot be accepted.
        except ValueError:
            # Notify the user to only input a valid coordinate.
            print("*-Input is not considered to be a coordinate")
            print("*-Coordinates are classified as a float-type")
            # Loop until a valid coordinate is inputted.
            invalid = True
            
    # Return the longitude value        
    return x

# Create a function for receiving and validating latitude input.
def get_y():
    
    # Declare a boolean variable for validation purposes.
    invalid = True
    
    while invalid == True:
        try:
            # Ask the user to enter the latitude.
            y = float(input("\nPlease enter latitude: "))
            print("'{}' has been accepted...".format(y))
            # Exit the while loop.
            invalid = False
        # Call upon a value error, if input cannot be accepted.
        except ValueError:
            # Notify the user to only input a valid coordinate.
            print("*-Input is not considered to be a coordinate")
            print("*-Coordinates are classified as a float-type")
            # Loop until a valid coordinate is inputted.
            invalid = True
            
    # Return the latitude value       
    return y

def display_info(hashtable, retlr, pstcode):
    # Utilizing the hashtable, display the values by using the information of...
    # the user retailer and postcode
    print("\n--------Location Information--------")
    print("Store name: {}".format(hashtable.get_value(retlr, pstcode)[0]))
    print("Address: {0} {1}".format(hashtable.get_value(retlr, pstcode)[1], hashtable.get_value(retlr, pstcode)[2]))
    print("Town: {}".format(hashtable.get_value(retlr, pstcode)[3]))
    print("Postcode: {}".format(hashtable.get_value(retlr, pstcode)[4]))
    print("Size Band: {}".format(hashtable.get_value(retlr, pstcode)[5]))
    print("------------------------------------")
            
def main():
    
    # Read the csv file...
    df = read_data()
    # Declare a list to store longitude values.
    long_list = []
    # Declare a list to store latitude values.
    lat_list = []
    # Declare a list to store tuples (to serve as points later on).
    data = []
    # Declare a list to store values in tuples for the hashtable.
    values_list = []
    
    # Iterate through the dataframe.
    for idx, row in df.iterrows():
        # Set appropriate variables names for each column value.
        lng = float(row['long_wgs'])
        lat = float(row['lat_wgs'])
        retlr = row['retailer']
        store = row['store_name']
        add1 = row['add_one']
        add2 = row['add_two']
        town = row['town']
        pstcode = row['postcode']
        sizebnd = row['size_band']
        # Add each row's longitude to the long_list.
        long_list.append(lng)
        # Add each row's latitude to the lat_list.
        lat_list.append(lat)
        # Add the point values in tuple form into the data list.
        data.append((lng, lat, retlr, pstcode))
        # Add each row's appropriate hashtable values (tuple form) into values list.
        values_list.append((retlr, store, add1, add2, 
                            town, pstcode, sizebnd))
    
    # Create the hashtable using the tuple values from the values list.
    hashtable = ST(values_list)
    
    # Determine the minimum and maximum longitude.
    maxX = max(long_list) + 0.01
    minX = min(long_list) + 0.01
    # Determine the minimum and maximum latitude.
    maxY = max(lat_list) + 0.01
    minY = min(lat_list) + 0.01
    
    # Calculate the center of the quadtree.
    centerX = float(abs(maxX - minX) / 2) + minX
    centerY = float(abs(maxY - minY) / 2) + minY
    
    # Calculate the distance between points.
    width = maxX - minX
    height = maxY - minY
    
    # Construct the rectangle/root.
    domain = Rectangle(TupleT(centerX, centerY, None, None), width, height)
    # Create the quadtree based on the newly-created rectangle.
    qtree = QuadTree(domain)
        
    # Create the TupleT (longitude, latitude, retailer, postcode).
    # Iterate through each tuple within the data list.
    for element in data:
        # Set the TupleT within a list.
        points = [TupleT(element[0], element[1], element[2], element[3])]
        for point in points:
            # Utilize the function to insert the point into the quadtree.
            qtree.insert(point)
    
    # Declare boolean variables for looping/validation purposes.
    loop1 = True
    loop2 = True
    
    # Construct a while loop to eventually return...
    # to the longitude and latitude prompts, if the user wants to.
    while loop1 == True:
        # Receive the longitude value.
        x = get_x()
        # Receive the latitude value.
        y = get_y()
        
        # Declare a list to insert the retailer and postcode values.
        found = []
        # Search throughout the QuadTree for the the longitude and latitude values.
        qtree.search(x, y, found)
        
        # Determine if the corresponding tuple has been found or not.
        if not found:
            # Notify the user that their input could not conceive a match.
            print("\nThere is no location listed at ({}, {})...".format(x, y))
        else:
            # Convert the both values within the found list into their unique id.
            # Since, values have been returned as their address in memory.
            memory_address = id(found)
            # Convert the ids into proper values.
            retailer = ctypes.cast(memory_address, ctypes.py_object).value[0]
            postcode = ctypes.cast(memory_address, ctypes.py_object).value[1]
            
            # Display the proper information of the given longitude and latitude...
            # by using the retailer and postcode values.
            display_info(hashtable, retailer, postcode)
        
        # Create another while loop to validate an upcoming prompt.
        while loop2 == True:
            # Ask the user if they would like to enter more coordinates.
            redo = input("\nWould you like to enter more coordinates? (Yes or No): ")
            # Convert the letters within input to all lowercase.
            redo = redo.lower()
            
            # Determine if the user entered 'Yes' or 'No'.
            if redo == "yes":
                # If 'Yes' was entered, return to the longitude and latitude prompts.
                loop1 = True
                # Exit the nested while loop.
                break
            # If 'No' was entered by the user...
            elif redo == "no":
                # Ensure to not return to either of the prompts.
                loop1 = False
                loop2 = False
                # Exit the main loop and nested loop.
                break
            else:
                # Let the user know that only 'Yes' or 'No' responses are acceptable.
                print("*-'Yes' or 'No' responses ONLY")
                # Return to the redo prompt.
                loop2 = True
    
    # Exit the program...
    print("\nExiting the program...")

# Utilize a try and except to ensure main executes without any errors.
try:
    main()
except AttributeError as ae:
    print(ae)