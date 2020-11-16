# Jude Fairchild
# Quadratic Formula Calculator

import math # import math because I need to square root

def roots(x, y, z):

    ans = [] # sets up array for answers

    # Discriminant 
    d = (y*y) - 4*x*z
    # Are roots real?
    if d < 0:
        print("The roots are not real, please restart the program.")
        return
    d = math.sqrt(d)

    # If so, do this:
    if d > 0:
        print("roots are real, good job!")
        # finishes off the quadratic formula
        root1 = (-y + d)/(2 * x) 
        root2 = (-y - d)/(2 * x)
        # adds roots into the array
        ans.append(root1)
        ans.append(root2)

        print(ans) # prints the array

print("Quadratic Solver")
print("ax^2 + bx + c")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

roots(a,b,c) # does "roots" program with a, b, and c
