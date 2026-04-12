def fizz_buzz(n: int) -> str:
    """Returns 'fizz' if n is divisible by 3, 
    'buzz' if n is divisible by 5, 'fizz buzz' if n is divisible by both, and the number itself otherwise.

    Args:
        n (int): The number to check.

    Returns:
        str: The result of the fizz buzz check.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)
    
print(fizz_buzz(3))   # fizz
print(fizz_buzz(5))   # buzz
print(fizz_buzz(15))  # fizz buzz
print(fizz_buzz(7))   # 7



