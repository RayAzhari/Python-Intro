# Rayan Azhari
# File: hw3.py
# Colaborator: Ali Azhari

print ("Hello there, please enter the a of the quadratic equation")
a = int(input())
print ("Please enter the b")
b = int(input())
print ("Finally, please enter the c")
c = int(input())

import math

d = int(b**2) - int(4*a*c)



if d < 0:
    print ("This has no solutions")
elif d == 0:
    s = -b/(2*a)
    print("The solution is" + str(s))
else:
    sol1 = int(-b-math.sqrt(d))/(2*a)
    sol2 = int(-b+math.sqrt(d))/(2*a)
    print("The solutions are  " + str(sol1) +   " " + str(sol2))