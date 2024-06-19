# main.py

from my_calculator import add, subtract

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Enter operation (+ or -): ").strip()
    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    else:
        print("Invalid operation")
        return
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()

print("sagar sonba padwal")
