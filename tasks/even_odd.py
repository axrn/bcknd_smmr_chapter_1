__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    even = sum(x for x in numbers if x % 2 == 0)
    odd = sum(x for x in numbers if x % 2 == 1)

    if odd == 0:
        return 0

    return even / odd
