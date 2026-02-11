def calculate (a, b, operator):
    if operator == 1:
        return a + b
    elif operator == 2:
        return a - b
    elif operator == 3:
        return a * b
    elif operator == 4:
        if b == 0:
            return "Error: Please do not divide by zero."
        return a / b


def show_menu():
    print("\nSelect Operation:")
    print ("1) +")
    print ("2) -")
    print ("3) *")
    print ("4) /")
    print ("0) exit")
    

def get_float(val):
    while True:
        try:
            return float(input(val))
        except ValueError:
            print("invalid paramters.")

def main():
    while True:
        show_menu()
        try:
            choice = int (input("Choice: "))

        except ValueError:
            print ("Invalid Input")
            continue

        if choice < 0 or choice > 4:
            print("Scelta fuori range") 
            continue

        if choice == 0:
            break
        
        a = get_float("First Number: ")
        b = get_float("Second Number: ")



        result = calculate (a, b, choice)
        print("Result:", result)



if __name__ == "__main__":
    main()