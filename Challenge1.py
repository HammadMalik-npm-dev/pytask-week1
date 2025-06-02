from functions import add, subtract, multiply, divide
from pyscript import organize_by_extension
from password_gen import generate_password

def calculator_menu():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    elif op == '*':
        print("Result:", multiply(a, b))
    elif op == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")

def file_organizer_menu():
    path = input("Enter folder path to organize: ")
    print(organize_by_extension(path))

def password_generator_menu():
    length = input("Enter password length (default 12): ")
    length = int(length) if length.isdigit() else 12
    print("Generated password:", generate_password(length))

def main():
    while True:
        print("\n--- CLI Toolkit ---")
        print("1. Calculator")
        print("2. File Organizer")
        print("3. Password Generator")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            calculator_menu()
        elif choice == '2':
            file_organizer_menu()
        elif choice == '3':
            password_generator_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
