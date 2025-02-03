def calculate_average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        try:
            total += float(number)
        except ValueError:
            print(f"Warning: Skipping non-numeric value: {number}")
            continue #skip to next iteration
    if total == 0 and len(numbers) > 0: #check if all the numbers are non-numeric values
        return 0
    average = total / len(numbers)
    return average

# Example usage:
my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average is: {average_empty}")

my_list_with_zero = [10,0,0,0,0]
average_zero = calculate_average(my_list_with_zero)
print(f"The average is: {average_zero}")

my_list_with_str = [10,20,'a',30,40,50]
average_str = calculate_average(my_list_with_str)
print(f"The average is: {average_str}")

my_list_with_str2 = ['a','b','c','d']
average_str2 = calculate_average(my_list_with_str2)
print(f"The average is: {average_str2}") 