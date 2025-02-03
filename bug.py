def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) #this will return 0 because the function handle the empty list case
print(f"The average is: {average_empty}")

my_list_with_zero = [10,0,0,0,0]
average_zero = calculate_average(my_list_with_zero) # this will return 2.0 which is 10/5
print(f"The average is: {average_zero}")