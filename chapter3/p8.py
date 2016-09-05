
people = input("How many people?")
pizza = input("How many pizzas do you have?")
pieces = input("How many pieces are in a pizza?")


total_pieces = int(pizza) * int(pieces)
each_pizza = int(total_pieces) / int(people)
remainder = int(total_pieces) - (int(people) * int(each_pizza))


print("%d people with %d pizzas"%(int(people), int(pizza)) )
print("Each person gets %d pieces of pizza."% int(each_pizza) )
print("There are %d leftover pieces."% int(remainder) )

