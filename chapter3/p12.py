import math

principal = int(input("Enter the principal : "))
interest = float(input("Enter the rate of interest : "))
period = int(input("Enter the number of years : "))

principal_and_interest = math.ceil(principal * (1 + (interest*0.01*period)))

print("After %d years at %.1f%%, the investment will be worth $%d"%(period, interest, principal_and_interest))



