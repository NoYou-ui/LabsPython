import math

num = int( input() )
amount = int( input() )
if num == 1:
    print( amount )
elif num == 2:
    print( amount / 1e+6 )
elif num == 3:
    print( amount / 1000 )
elif num == 4:
    print( amount * 1000 )
elif num == 5:
    print( amount * 100 )