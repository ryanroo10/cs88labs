# Question 1-3
def second_max(lst):
    """
    Return the second highest number in a list of positive integers.

    >>> second_max([3, 2, 1, 0])
    2
    >>> second_max([2, 3, 3, 4, 5, 6, 7, 2, 3])
    6
    >>> second_max([1, 5, 5, 5, 1])
    5
    >>> second_max([5, 6, 6, 7, 1])
    6
    >>> second_max([5, 6, 7, 7, 1])
    7
    """

    lst.sort(reverse = True)
    return lst[1]




from math import sqrt

def is_square(n):
    return float(sqrt(n)) == int(sqrt(n))

def squares(seq):
    """Returns a new list containing elements of the original list that are
    perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> squares(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    def perfect_square(x):
        y = x ** .5
        return int(y + .5) ** 2 == x
    return list(filter(perfect_square, seq))




def pairs(n):
    """Returns a new list containing two element lists from values 1 to n
    >>> pairs(1)
    [[1, 1]]
    >>> x = pairs(2)
    >>> x
    [[1, 1], [2, 2]]
    >>> pairs(5)
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    >>> pairs(-1)
    []
    """
    return [[x, x] for x in list(range(1, n + 1))]



# Question 4

def converter(temperatures, convert):
    """Returns a sequence that converts each Celsius temperature to Fahrenheit

    >>> def convert(x):
    ...     return 9.0*x/5.0 + 32
    >>> temperatures = [10, 20, 30, 40, 50]
    >>> converter(temperatures, convert)
    [50.0, 68.0, 86.0, 104.0, 122.0]
    """
    def convert(x):
        return 9.0*x/5.0 + 32
    return list(map(convert, temperatures))



# Question 5

from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    for n in s:
        base = reducer(base, n)
    return base 



# Question 6

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> def identity(x):
    ...     return x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h



# Question 7

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> def square(x):
    ...     return x * x
    >>> def triple(x):
    ...     return x * 3
    >>> def increment(x):
    ...     return x + 1
    >>> def identity(x):
    ...     return x
    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    def h(g):
        if g(x) == f(x):
            return True
        return False
    return h



# Optional, Extra Credit.
def lab2_extra_credit():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-week1
  """
  okpy_email = "my_examil@berkeley.edu"
  practice_result_code = "00000xxxxx"
  return (okpy_email, practice_result_code)
