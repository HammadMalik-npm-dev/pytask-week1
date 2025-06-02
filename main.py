from functions import get_operation

def main():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "5":
            break

        operation = get_operation(choice)
        if not operation:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = operation(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Unexpected error occurred.")

if __name__ == "__main__":
    main()
