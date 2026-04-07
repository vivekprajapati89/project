#input we need 

#total rent of hostel/flat
#total spend in snack
#electricity unit spend
# charge per unit 
# person live in hostel/flat 
 

#output
#total amount is and you have to pay



rent =int(input("enter the rent you pay for flat\hostel="))
food=int(input("enter amount that you pay for snack= "))
electricity_charge=int(input("enter total electricity unit spend= "))
charge_per_unit=int(input("enter the charge per unit ="))
persons=int(input("enter how much live in flat\hostel="))

total_electricity=electricity_charge* charge_per_unit


total=rent+food+total_electricity
charge_person=total/persons


print(f"total amount is {total} , and you each person pay",charge_person)