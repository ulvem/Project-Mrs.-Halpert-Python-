def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd
print(even_or_odd(0))  # Output: Even
print(even_or_odd(-3)) # Output: Odd

def basic_operations(operation, value1, value2):
    if operation == 'add':
        return value1 + value2
    elif operation == 'subtract':
        return value1 - value2
    elif operation == 'multiply':
        return value1 * value2
    elif operation == 'divide':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Examples of usage:
print(basic_operations('add', 10, 5))       # Output: 15
print(basic_operations('subtract', 10, 5))  # Output: 5
print(basic_operations('multiply', 10, 5))  # Output: 50
print(basic_operations('divide', 10, 5))    # Output: 2.0
print(basic_operations('divide', 10, 0))    # Output: Error: Division by zero
print(basic_operations('modulus', 10, 5))   # Output: Error: Invalid operation

def total_points(results):
    total = 0
    for result in results:
        x, y = map(int, result.split(':'))
        if x > y:
            total += 3
        elif x == y:
            total += 1
        # No need to add points for a loss (x < y)
    return total

def largest_number(a, b, c):
    # Evaluate all possible combinations
    combinations = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + (b * c),
        (a * b) + c
    ]
    # Return the maximum value from the combinations
    return max(combinations)

# Example usage
a, b, c = 1, 2, 3
print(largest_number(a, b, c))  # Output: 9


# Examples of usage:
matches = ["3:1", "2:2", "0:1", "4:0", "1:1"]
print(total_points(matches))  # Output: 8

def print_star_grid(rows, cols):
    for i in range(rows):
        print("* " * cols)
    print()

# Example usage:
print_star_grid(4, 4)

def index(array, n):
    # Check if the index n is within the bounds of the array
    if n < len(array):
        # Return the Nth power of the element at position n
        return array[n] ** n
    else:
        # Return -1 if the index is out of bounds
        return -1

# Example usage
array = [1, 2, 3, 4, 5]
n = 2
print(index(array, n))  # Output: 9 (3^2)

n = 5
print(index(array, n))  # Output: -1 (index out of bounds)

def quarter_of_the_year(month):
    if 1 <= month <= 3:
        return 1  # Q1: January, February, March
    elif 4 <= month <= 6:
        return 2  # Q2: April, May, June
    elif 7 <= month <= 9:
        return 3  # Q3: July, August, September
    elif 10 <= month <= 12:
        return 4  # Q4: October, November, December
    else:
        return -1  # Invalid month

# Example usage
print(quarter_of_the_year(2))  # Output: 1
print(quarter_of_the_year(5))  # Output: 2
print(quarter_of_the_year(8))  # Output: 3
print(quarter_of_the_year(11)) # Output: 4
print(quarter_of_the_year(13)) # Output: -1 (invalid month)

def century(year):
    # Calculate the century by dividing the year by 100 and rounding up
    return (year + 99) // 100

# Example usage
print(century(1705))  # Output: 18
print(century(1900))  # Output: 19
print(century(1601))  # Output: 17
print(century(2000))  # Output: 20
print(century(89))    # Output: 1

def form_the_minimum(digits):
    # Remove duplicates by converting the list to a set, then back to a list
    unique_digits = list(set(digits))
    # Sort the digits in ascending order
    unique_digits.sort()
    # Combine the sorted digits into a single number
    minimum_number = int(''.join(map(str, unique_digits)))
    return minimum_number

# Example usage
digits = [3, 1, 4, 1, 5, 9]
print(form_the_minimum(digits))  # Output: 13459

digits = [5, 7, 5, 9, 1]
print(form_the_minimum(digits))  # Output: 1579


