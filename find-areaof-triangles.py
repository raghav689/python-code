# python program to find the area of triangkes
a = 5
b = 6
c = 7

# uncommemt below to take inputs from the user
# = float(input('Enter first side: '))
# b = float(input('Enter second  side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('the area of the triangles is %0.2f' %area)