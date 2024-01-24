a = float(input("Enter a : "))
b = float(input("Enter b : "))

choice = input('''Enter choice (Add +,
               Subtract -,
               Multiplication *,
               Division /,
               Remainder %) : ''').lower()

if choice == '+' or choice == "add":
    c=a+b
    print(c)

elif choice == '-' or choice == "subtract":
    c=a-b
    print(c)

elif choice == '*' or choice=="multiplication":
    c=a*b
    print(c)

elif choice == '/' or choice=="division":
    c=a/b
    print(c)

elif choice == "%" or choice=="remainder":
    c=a%b
    print(c)

else:
    print("Wrong input !")