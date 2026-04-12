def sum_numbers(*values: float) -> float:
    """Returns the sum of all the values passed as arguments."""
    total = 0
    for value in values:
        total += value
    return total
print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(10, 20, 30, 40))  # 100
print(sum_numbers())  # 0
print(sum_numbers(12.5, 3.147, 98.1))  # 113.747
