#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# A=πr(r+h2+r2)
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

r = input("whats the radius?")
h = input("whats the height?")

r = float(r)
h = float(h)

print(3.141592653589793238462643383279502884197 * r * ( r + (h ** 2 + r ** 2 ) ** 0.5 ) )
