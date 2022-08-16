

print ("Hello there, please enter the a of the quadratic equation")
a = int(input())
print ("Please enter the b")
b = int(input())
print ("Finally, please enter the c")
c = int(input())



d = int(b**2) - int(4*a*c)

sol1 = int(-b-(d))/(2*a)
sol2 = int(-b+(d))/(2*a)
if d < 0:
    print ("This has no solutions")
else:


    print(sol1)
    print(sol2)