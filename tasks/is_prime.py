__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True
