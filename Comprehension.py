def odd_numbers_under_value():
    user_input = int(input("Enter a number: "))
    odd_numbers = [num for num in range(user_input) if num % 2 != 0]
    print(f"List of odd numbers under {user_input}: {odd_numbers}")

def capitalize_fruits():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    capitalized_fruits = [fruit.capitalize() for fruit in fruits]
    print(f"Capitalized fruits: {capitalized_fruits}")

if __name__ == "__main__":
    odd_numbers_under_value()
    capitalize_fruits()