
from item import Item
from menu import Menu
items = []
id_count = 1

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):
    print_header(header_text)
    print("-" * 70)
    print("ID  | Item Title                | Category        | Price     | Stock")
    print("-" * 70)

    for item in items:
        print(str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15) + " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))


def register_item():
    global id_count # importing the global variable, into fn scope

    print_header(" Register new Item")
    title = input("Please input the Title: ")
    category = input("Please input the Category: ")
    price = float(input("Please input the Price: "))
    stock = int(input("Please input the Stock: "))

    #validations

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    id_count += 1
    items.append(new_item)
    print("Item Created!!")

def update_stock():
    # show the user all the items
    # ask for the desired id
    #get the element from the array with that id
    #ask for the new stock
    #update the stock of the element
    print_all("Choose an Item from the list")
    id = input("\nSelect an ID to update its stock: ")
    # find the element = False
    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("Please input new stock value: ")
            item.stock = int(stock)
            found = True
    
    if(not found):
        print("** Error: ID doesn't exist, try again")


opc = ""
while(opc != "x"):
    Menu()
    opc = input("Select an option: ")
    if(opc == "x"):
        break #break the loop

    elif(opc == '1'):
        register_item()

    elif(opc == '2'):
        print_all("Lists of All Item")
    
    elif(opc == '3'):
        update_stock()

    if(opc != "x"):
        input("\n\nPress Enter to continue..")
