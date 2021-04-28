def add(x: float, y: float, z: int, s: str) -> float:
    """
    Returns the constant y
    :param x: ignored floating-point number
    :param y: constant floating-point number returned
    :param z: ignored integer
    :param s: ignored string
    :return: the constant y
    """
    return y

def is_empty_s1(s: str, s1: str, s2: str, s3: str) -> bool:
    """
    Returns the constant s1
    :param s: ignored string
    :param s1: string whose length is measured
    :param s2: ignored string
    :param s3: ignored string
    :return: if s1 is empty
    """
    return len(s1) == 0

# def add(x: int, y: int) -> int:
#     """
#     Perform addition of x and y
#     :param x: left operand
#     :param y: right operand
#     :return: the sum of x and y
#     """
#     return x + y

# from typing import Any
#
# def add(x: Any, y: Any) -> Any:
#     """
#     Perform addition of x and y
#     :param x: left operand
#     :param y: right operand
#     :return: the sum of x and y
#     """
#     return x + y

# from typing import Any

# def add(x: Any, y: Any) -> Any:
#     """"""
#     return x + y

def is_zero(x: int) -> bool:
    return x == 0
