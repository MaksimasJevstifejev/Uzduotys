def calculate_average(numbers_list):
    result = []
    for string, numbers in numbers_list:
        average = sum(numbers) / len(numbers)
        result.append((string, average))
    return result

data = [
    ("banana", [1, 2, 6]),
    ("apple", [4, 5, 9]),
    ("orange", [2, 8, 11])
]

averages = calculate_average(data)
print(averages)
