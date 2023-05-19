from functools import reduce

def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

filename = "numbers.txt"

with open(filename, "r") as file:
    numbers = [int(line.strip()) for line in file]

average = calculate_average(numbers)

print("Average:", average)

output_filename = "average.txt"

with open(output_filename, "w") as file:
    file.write(str(average))
