
def cal(length, width):
    feet_square = length * width
    area = feet_square/3.3
    
    meter = area*area*0.09290304
    meter_square = meter ** 0.5
    
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
