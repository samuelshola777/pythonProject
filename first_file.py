
if __name__ == '__main__':
# Calculate the area and circumference of a circle from it's radis.
# step 1: prompt for a radius.
# step 2 : apply the area formula.
# step 3 : print out the results


import math

radius_str = input("enter the radius of your circle: ")
radius_int = int(radius_str)


circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int **2)


print("the cirumference is: ", circumference,", and is :",area)
