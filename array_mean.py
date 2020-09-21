## Get the mean of an array
##
## It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
## Return the average of the given array rounded down to its nearest integer.
## The array will never be empty.

import numpy as np
import math

def array_mean(array):
    return math.floor(np.mean(array))


array_test = [13, 4, 33, 9, 12.4, 4.5, 11.7]
print("The array mean is " + str(array_mean(array_test)))
