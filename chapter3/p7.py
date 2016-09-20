
def cal(length, width): 
    meter_square = length * width * 0.09290304
    return meter_square


def main():
    feet_length = input("What is the length of the room in feet?")
    feet_width = input("What is the width of the room in feet?")
    
    length = int(feet_length)
    width = int(feet_width)
    print("You entered dimentions of %d feet by %d feet" % (length, width))

    meter_square = cal(length, width)
    print("The area is\n %d square feet\n %.4f square meters."% (length*width, meter_square) )


if __name__=="__main__":
    main()
