#write ADD function



#write SUBTRACT function



#write MULTIPLICATION function
def multi(x,y):
    return x * y


#write DIVISION function



#write REMAINDER function




#Don't change anything below this line
while True:
    print("MENU")
    print("Choose your option")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(add(a,b))
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(sub(a,b))
    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(multi(a,b))
    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(div(a,b))
    elif choice == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(rem(a,b))
    else:
        print("Exiting.......")
        break