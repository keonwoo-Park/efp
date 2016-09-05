import math

length = input("length : ")
width = input("width : ")
square = int(length) * int(width)

paint = math.ceil(square/9)

print("You will need to purchase %d liters of \npaint to cover %d square meters."%(paint, square))

