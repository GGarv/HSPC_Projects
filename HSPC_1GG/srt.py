s=1.0
x=6.0
for k in range(20):
	s=0.5(s+x/s)
print("Using Newton's method: ",s)

from math import sqrt
print("Using inbuilt sqrt fun: ".sqrt(x))

