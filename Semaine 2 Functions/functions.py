def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exponent: int) -> int:
    return base ** exponent

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
print(multiply(3, 4))  # 12
print(divide(10, 2))   # 5.0
print(power(2, 3))     # 8
print(factorial(5))    # 120
print(fibonacci(10))   # 55


def _is_palindrome(s: str) -> bool:
    cleaned = ''.join(c for c in s.casefold() if c.isalnum())
    return cleaned == cleaned[::-1]

print(_is_palindrome("A man a plan a canal Panama"))  # True
print(_is_palindrome("Hello"))  # False 
print(_is_palindrome("No 'x' in Nixon"))  # True
print(_is_palindrome("Radar"))  # True