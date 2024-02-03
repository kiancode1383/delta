import math
def Delta(a,b,c):
    x = ((b*b) - (math.sqrt(4*a*c))) / (2*a)
    return x

print(Delta(4,4,4))