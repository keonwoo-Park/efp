
length = input("length : ")
width = input("width : ")
square = int(length) * int(width)

paint = round((square/9)+0.5)

print("You will need to purchase %d liters of \npaint to cover %d square meters."%(paint, square))
