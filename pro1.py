'''calculator'''
try :
    a=int(input("enter value a: "))
    b=int(input("enter value b: "))
    print("what kind of operation woud you like to d0 ?\nPress + for addition \nPress - for subtraction \nPress * for multiplication \nPress / for divition \n ")
    o=input("enter your operation: ")
    match o:
        case "+":
            print(f" the result is {a+b}")
        case "-":
            print(f" the result is {a-b}")
        case "*":
            print(f" the result is {a*b}")
        case "/":
            try:
                print(f" the result is {a/b}")
            except ZeroDivisionError:
                print("please don't divide by zero")
        case _:
            print(" invalid operation ")
            
except Exception:
    print (" enter valid value of a and b ")
