import pandas as pd
import ctypes
import pprint

class ST:
    def __init__(self, elements):
        # Create a list of buckets. 
        # Account for load factor when trying to find a reasonable bucket size.
        # From the csvfile, there are 37 different retailers, hence 37 different keys.
        # The load factor should be below 1.0 and is calculated by: total keys / number of buckets.
        # The bucket size should NOT be under 37!
        # This is why I have chosen 107 total buckets in my structure.
        # The load factor is 37 / 107 which equals 0.34579439252.
        self.bucket_size = 107
        # Bucket amount will equate to the number of tuples inside the given list
        self.buckets = [[] for i in range(self.bucket_size)]
        # Assign all tuples a specific bucket
        self._assign_buckets(elements)
    
    # Create a hash function
    def get_hash(self, key):
        # Declare a hash value variable and set it equal to 0.
        hashval = 0
        # Iterate through each letter in the key.
        for char in key:
            # The hash value will be the sum of each letter's ascii value.
            hashval += ord(char)
        # Return the remainder of the hash value divided by the bucket amount.
        # The remainder will serve has the hash value of the key. 
        return hashval % self.bucket_size
    
    # Assign each tuple to a designated bucket.
    def _assign_buckets(self, elements):
        # Iterate through the tuple and set the bucket to correspond with the key hash value.
        for key, value1, value2, value3, value4, value5, value6 in elements:
            index = self.get_hash(key)
            # Add the tuple to the corresponding bucket.
            self.buckets[index].append((value1, value2, value3, value4, value5, value6))
    
    # Return the all values that correlate with the key's hash value and x & y coordinate.
    # Values: The retailer's store name, address, town, postcode & size band.
    def get_value(self, input_key, postcode_value):
        # Find the values by locating the key hash value.
        index = self.get_hash(input_key)
        # Declare and set a variable as the corresponding bucket to the key's hash value.
        bucket = self.buckets[index]
        # Iterate through each tuple within the bucket to find a match.
        for value1, value2, value3, value4, value5, value6 in bucket:
            # Postcode must match with the postcode_val.
            if value5 == postcode_value:
                # Return all of the values within the tuple.
                return(value1, value2, value3, value4, value5, value6)
        return None
    
    def __str__(self):
        # Return a printable representation of object.
        return pprint.pformat(self.buckets) 