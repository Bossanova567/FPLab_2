"""Program to find out if a number is simple or not"""
import sympy

def recursive_func(x: int, n: int = 2) -> bool:
    """
    Returns a boolean value, which tells us, if number is simple or not.

    Arguments:
        x (int): Number, that should be determined, if it is simple or not.
        n (int): Index, which function uses in recursion.

    Returns:
        Boolean value. True, if number is simple. False, if number is not simple. None, if number is not natural or is one.

    """
    if x <= 1:
        return None
    if x == 2: return True
    if x % n == 0:
        return False
    if n * n > x:
        return True
    return recursive_func(x, n + 1)


def non_recursive_func(x: int) -> bool:
    """
    Returns a boolean value, which tells us, if number is simple or not.

    Arguments:
        x (int): Number, that should be determined, if it is simple or not.

    Returns:
        Boolean value. True, if number is simple. False, if number is not simple. None, if number is not natural or is one.

    """
    n = 2
    if x <= 1:
        return None
    while n < x:
        if x % n == 0:
            return False
        n += 1
    return True


try:
    x = int(input("Enter a number:"))
    result = recursive_func(x)
    if result is None:
        print("Your number has to be natural and greater than 1")
    elif result:
        print("Your number is simple")
    else:
        print("Your number is not simple")
except ValueError:
    print("Your number should be integer")
