x=5
y=9
z=1

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

z = x
x = y
y = z

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))
print("The value of z after swapping: {}".format(z))