import math

amountOfPositives = 0
a = int( input() )
b = int( input() )
c = int( input() )
if a > 0:
    amountOfPositives += 1
elif b > 0:
    amountOfPositives += 1
elif c > 0:
    amountOfPositives += 1
print(amountOfPositives)