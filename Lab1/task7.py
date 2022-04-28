import math

angle = 90
side1 = 180
side2 = 240
side3 = math.sqrt( (side1**2) + (side2**2) )
S = 0.5 * (side1*side2) * math.sin(math.pi/2)
print( side3, S )