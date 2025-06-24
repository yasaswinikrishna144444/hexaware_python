def division():
    try:
        x= int(input("Enter a number: "))
        y = int(input("Enter the divider: "))
        result = x / y
        print("result is: ", result)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("You can't divide by zero")
division()



