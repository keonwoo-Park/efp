
euros = int(input("How many Euros are you exchanging? "))
euros_rate = float(input("What is the exchange rate? "))
dollar_rate = 100
dollar = (euros * euros_rate)/100

print("%d Euros at an exchange rate of %.2f is \n%.2f dollars"%(euros, euros_rate, dollar)) 
