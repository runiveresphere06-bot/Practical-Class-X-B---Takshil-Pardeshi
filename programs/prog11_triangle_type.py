# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 11: Find whether a triangle is equilateral, isosceles or scalene

a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))

# A triangle is possible only if the sum of any two sides is greater than the third
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("It is an Equilateral triangle (all sides equal).")
    elif a == b or b == c or a == c:
        print("It is an Isosceles triangle (two sides equal).")
    else:
        print("It is a Scalene triangle (all sides different).")
else:
    print("These sides cannot form a triangle.")
