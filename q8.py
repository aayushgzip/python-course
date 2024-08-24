
def print_purchase(path):
    dictitem = load_vending(path)
    if not dictitem:
        print("no item loaded")
        return
    while True:
        item = input("enter Item you would like to buy: ").strip()
        if item in dictitem:
            price = dictitem[item]
            print("your total amount is: ",price)
            try:
                input_price = int(input("\nenter money: "))
                if input_price > 0:
                    if(input_price<price):
                        print("\n insufficient balance ")
                    elif(input_price==price):
                        print("/n Thank you for your purchase. Enjoy!")
                        break
                    else:
                        change= input_price - price
                        print("Thank you for your purchase. Enjoy!")
                        print(f"dont forget your change: {change} rs")
                        break
                else:
                    print("money cannot be negative")
            except ValueError:
                print("bad input try again")
        else:
            print(f"available items are {list(dictitem.keys())} ")
            print("try again")
            
    return

def load_vending(file_path):
    items = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    item, price = line.split('|') 
                    items.update({item:int(price)})
                    
    except FileNotFoundError:
        print("file does not exist")
    return items    
file_path = 'Items.txt'    
print_purchase(file_path)
    
