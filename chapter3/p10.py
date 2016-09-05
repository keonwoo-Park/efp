


def cal(price1, price2, price3, item1_quantity, item2_quantity, item3_quantity):
    subtotal = (price1 * item1_quantity) + (price2 * item2_quantity) + (price3 * item3_quantity)
    tax = subtotal * 0.055
    total = subtotal + tax
    
    value = [subtotal, tax, total]
    return value


def result_print(total_price):
    print("subtotal : $%.2f"%total_price[0])
    print("tax : $%.2f"%total_price[1])
    print("total : $%.2f"%total_price[2])
    

def main():
    price1 = int(input("Price of item 1: "))
    item1_quantity = int(input("Quantity of item 1: "))
    price2 = int(input("Price of item 2: "))
    item2_quantity = int(input("Quantity of item 2: "))
    price3 = int(input("Price of item 3: "))
    item3_quantity = int(input("Quantity of item 3: "))

    
    total_price = cal(price1, price2, price3, item1_quantity, item2_quantity, item3_quantity);
    result_print(total_price)


if __name__=="__main__":
    main()
