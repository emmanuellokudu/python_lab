from utils import square, is_even, celsius_to_fahrenheit


def main():
    try:
        number = int(input("Enter a number: "))

        print(f"Square: {square(number)}")

        if is_even(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

        fahrenheit = celsius_to_fahrenheit(number)
        print(f"{number}°C is {fahrenheit:.2f}°F.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
    