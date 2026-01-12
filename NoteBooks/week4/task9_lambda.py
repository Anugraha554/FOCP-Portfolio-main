import math
hypot = lambda a,b: math.sqrt(a*a + b*b)
print(type(hypot))

to_seconds = lambda h,m=0: h*3600 + m*60
print(to_seconds(0,2))
print(to_seconds(2))
