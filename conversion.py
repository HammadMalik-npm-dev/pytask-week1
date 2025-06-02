def main():
    print("Unit Conversion Tool")
    print("1. Inches to Centimeters")
    print("2. Pounds to Kilograms")
    print("3. Fahrenheit to Celsius")
    print("4. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "4":
            break

        values = input("Enter values separated by spaces: ").split()

        try:
            numbers = list(map(float, values))

            if choice == "1":
                result = list(map(lambda x: x * 2.54, numbers))
            elif choice == "2":
                result = list(map(lambda x: x * 0.453592, numbers))
            elif choice == "3":
                result = list(map(lambda x: (x - 32) * 5/9, numbers))
            else:
                print("Invalid choice")
                continue

            print("Converted values:", result)
        except ValueError:
            print("Please enter numeric values only.")

if __name__ == "__main__":
    main()
