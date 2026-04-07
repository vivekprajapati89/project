menu={"pasta":100,
       "coffee":80,
       "burger":120,
       "salad":50,
       "maggie":40,
       "pizza":100,}
print("WELCOME TO OUR RESTAURANT\n")
print("NOW WE HAVE AVAILABLE ")
print("pasta:RS100\ncoffee:RS80\nburger:RS120\nsalad:RS50\nmaggie:RS40\npizza:RS100")
order_total=0
item_1=input("enter your first item").strip().lower()
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} should be addded ")
else:
    print(f"your item {item_1} are not availabe yet:")

item_2=input("do you want to order another thing (YES/NO)").strip().lower()
if item_2=="yes":
    item2=input("enter your item").strip().lower()
    if item2 in menu:
        order_total+=menu[item2]
        print(f"item {item2} should be added ")
    else:
        print(f"item {item2 } are not available in our retaurant ")

print(f"total amount you pay {order_total}")