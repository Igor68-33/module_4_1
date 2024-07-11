from math import inf

def divide(first, second):
    """

    :param first:
    :param second:
    :return first / second
    если second=0, то результат бесконечность.
    """
    if second == 0:
        return inf
    return first / second

# print(__name__)