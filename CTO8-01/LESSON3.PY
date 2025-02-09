items={
    "notebook":2.50,
    "pencil":0.50,
    "pen":1.20,
    "ruler":1.50,
    "eraser":0.50,
    "writing pad":2.50,
    "marker":2.00,
    "glue":3.00,
    "calculator":35.00
}
def show_menu(menu):
    print("-----Welcome to the best bookshop in the world----")
    print("This is our menu")
    print("Please note: There is a 10% discount for orders above $20")
    for item,price in menu.items():
        print(f"{item:^20} :$ {price:.2f}")
    print("-----This is the end of the menu-----")

def take_order(order,menu,customer_order):
        if order in menu:
            print(f"{order} :$ {menu[order]}")
            quantity=input(f"How many {order}s would you like?")
            print(f"{quantity} {order}s has been added to your order")
            customer_order[order]={"quantity":quantity,"value":int(quantity)*menu[order]}
            return customer_order
        else:
            print(f"Sorry we do not have {order}")
            return customer_order

def tallycost(customer_order,cost,newprice):
    print("---Order summary---")
    for item,price in customer_order.items():
        quantity=price["quantity"]
        value=price["value"]
        cost+=float(value)
        print(f"{quantity} {item}(s) :$ {price}")
        if price>20:
            newprice=(90/100)*price
            print("-----------------")
    print(f"Total cost: ${newprice}")
            
        
    print("-----------------")
    print(f"Total cost: ${cost}")

  

    

customer_order={}
cost=0
show_menu(items)
order=input("Enter order, type 'end' to end.")
while order!="end":
    take_order(order,items,customer_order)
    order=input("Enter order, type end to end.")

else:
    tallycost(customer_order,cost)
print("Will you be paying by cash or card?")

