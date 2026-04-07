def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division (a,b):
    return a/b



a=int(input("enter first number"))
b=int(input("enter second number "))

# item ={
#     "addition":"+",
#     "subtraction":"-",
#     "multiplication":"*",
#     "division":"/",
# }
print ("choose operation:\naddition:+\nsubtraction:-\nmultiplication:*\ndivision:/")

perform=input("enter what you want to perform ").strip().lower()

if perform=="addition" or perform == "+" :
     print("the addition of a number is : ",addition(a,b))
elif perform== "subtraction" or perform== "-":
    print("the subtraction of number is : ",subtraction(a,b))
elif perform== "multiplication" or perform=="*":
    print("the multiplication of a number : ",multiplication(a,b))
elif perform=="division" or perform=="/":
    if b==0:
        print("number can't divided by zero")
    else:
        print("the division a number is :",division(a,b))

else:
    print("yours are not perform any operation ")



# print("the subtraction of number is : ",subtraction(a,b))
# print("the addtion of a number is : ",addition(a,b))
# print("the multiplication of a number : ",multiplication(a,b))
# print("the division a number is :",division(a,b))


   
# print(subtraction(2,4))