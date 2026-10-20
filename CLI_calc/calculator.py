## This is a project that builds a CLI calculator for mathematical operations.
def add(a,b):
    return a + b 
def subtract(x,y):
    return x - y
def multiply(r,t):
    return r * t 
def divide(m,g):
    if g == 0:
        return "Error Division by zero."
    return m / g
    
def calculator():
    while True:
        print("\n==== Welcome to ZAD calculator ====")
        print("1. Addition (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit") 
        
        choice = input("Choose an option from the above menu (1-5): ")
        
        if choice == "5":
                print("Exiting the calculator. Goodbye")
                break
        if choice in ("1","2","3","4"):
            try:
                digit1 = float(input("Enter a number: "))
                digit2 = float(input("Enter a number: "))
            except ValueError:
                print("Enter a valid number")
                continue
            if choice == "1":
                print(f"Result: {digit1} + {digit2} = {add(digit1, digit2)}")
            elif choice == "2":
                print(f"Result: {digit1} - {digit2} = {subtract(digit1, digit2)}")
            elif choice == "3":
                print(f"Result: {digit1} * {digit2} = {multiply(digit1, digit2)}")
            elif choice == "4":
                print(f"Result: {digit1} / {digit2} = {divide(digit1, digit2)}")  
        else:
            print("Invalid option, choose a valid option from menu above")

if __name__ == "__main__":
    calculator()