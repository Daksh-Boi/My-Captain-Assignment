# 1. Why we have the name float :
# Decimal values are called floating point values in programming languages
# because of the fact that there is no fixed number between two integer numbers
# or a fixed number of digits before and after the decimal point.

# 2. Use Terminal to open Apps :
#      1. cd C:\Users\Administrator\AppData\Local\atom
#      2. .\atom.exe


# 3. Use the arithmetic operators with 4 different SETS of values :
x = int(input("Input value of integer one"))
y = int(input("Input value of integer two"))
print("Sum of " ,(x), " and ",(y) ," is = ", (x+y) )

x = int(input("Input value of integer one"))
y = int(input("Input value of integer two"))
print("Difference between " ,(x), " and ",(y) ," is = ", (x-y) )

x = int(input("Input value of integer one"))
y = int(input("Input value of integer two"))
print("Product of " ,(x), " and ",(y) ," is = ", (x*y) )

x = int(input("Input value of integer one"))
y = int(input("Input value of integer two"))
print("Quotient of " ,(x), " when divided by ",(y) ," is = ", (x/y) )

x = int(input("Input value of integer one"))
y = int(input("Input value of integer two"))
print("Remainder of " ,(x), " when divided by ",(y) ," is = ", (x%y) )

#4. Find the area of a circle :
radius = float(input("Input the radius of the circle"));
area =22/7* radius * radius;
print( "area of the circle = ",(area));


 #5. File extension program:
fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[1])
