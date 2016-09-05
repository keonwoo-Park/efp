import math


principal = int(input("What is the principal amount?  "))
rate = float(input("What is the rate : "))
period = int(input("What is the number of years : "))
interest_count = int(input("What is the number of times the interest is compounded per year : "))


principal_and_interest = principal*(1+(rate/100)/interest_count)**(interest_count*period)
print("$%d invested at %.1f%% for %d years compouned %d times year is $%.2f"\
    %(principal,rate,period,interest_count, principal_and_interest) )
