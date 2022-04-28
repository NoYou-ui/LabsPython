import math

n1 = int( input() )
n2 = int( input() )
n3 = int( input() )
n4 = int( input() )
if n1 == n2 == n3:
    print("4")
elif n1 == n2 == n4:
    print("3")
elif n1 == n3 == n4:
    print("2")
elif n2 == n3 == n4:
    print("1")
