def factorial(n: int) -> int:
    """Returns the factorial of a non-negative integer n.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # 120
print(factorial(0))  # 1    
print(factorial(1))  # 1
