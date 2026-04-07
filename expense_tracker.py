expenses=[]


while True:
    print("=====Menu=====")
    print("1.Add Expense:")
    print("2.View All Expenses:")
    print("3.View Your Total Expenses:")
    print("4.Exit:")


    choice=int(input("enter your choice :"))



    if (choice==1):
        date=input("enter the date you spend the money: ")
        category=input("which type of category you spend your money (travel,food,shopping): ")
        description=input("if you like to add more detail: ")
        amount=input("how much you spend ??: ")

        expense={
        "date":date,
        "category":category,
        "description":description,
        "amount":amount
        }


        expenses.append(expense)

        print("\n done bruhhh ! your expenses is added ")



    elif (choice == 2):
    
        if len(expenses)==0:
            print("go and spend some money then come !!!")
        else:
            print("=====here is your expensive=====")
            count=1
            for spend in expenses:
                print(f"spend number {count} --> {spend["date"]}, {spend["category"]},{spend["description"]},{spend["amount"]}")
                count+=1
    

    elif (choice==3):
        total=0
        for kharcha in expenses:
            total=total+kharcha["amount "]
        print("\n TOTAL SPEND AMOUNT IS :",total)
    

    elif (choice==4):
        print("thanks for using our expense tracker !!")
        break

    else:
        print("INVAILD NUMBER !!! PLEASE ENTER THE CORRECT NUMBER ")


    
