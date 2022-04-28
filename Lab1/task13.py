import math

x1 = float( input() )
x2 = float( input() )
y1 = float( input() )
y2 = float( input() )
AB = abs( y2 - y1 )
BC = abs( x2 - x1 )
P = 2*( AB + BC )
S = AB * BC
print(P, S)