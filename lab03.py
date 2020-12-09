# Question 1-4

def where_above(lst, limit):
    """
    where_above behaves like table.where(column, are.above(limit)).
    The analogy is completed if you think of a column of a table as a list and return the filtered column instead of the entire table.

    >>> where_above([1, 2, 3], 2)
    [3]
    >>> where_above(range(13), 10)
    [11, 12]
    >>> where_above(range(123), 120)
    [121, 122]

    """
    return [x for x in lst if x > limit]



def minmax(s):
    """Return the minimum and maximum elements of a non-empty list. Hint: start
    with defining two variables at the beginning. Do not use the built in
    max or min functions

    >>> minmax([1, 2, -3])
    [-3, 2]
    >>> x = minmax([2])
    >>> x
    [2, 2]
    >>> minmax([4, 5, 4, 5, 1, 9, 0, 7])
    [0, 9]
    >>> minmax([100, -10, 1, 0, 10, -100])
    [-100, 100]
    """
    def highest(n):
        mymax = n[0]
        for i in n:
            if i > mymax:
                mymax = i
        return mymax
    def lowest(n):
        mymin = s[0]
        for j in n:
            if j < mymin:
                mymin = j
        return mymin
    return [lowest(s), highest(s)]


def common_member(lst1, lst2):
    """
    Returns true if there are any common members between
    lst1 and lst2.
    >>> common_member([5, 3, 2, 1], [1, 9, 3, 4, 5])
    True
    >>> common_member([17, 18, 24], [23, 21, 22, 27, 29, 5])
    False
    >>> common_member([5, 7], [7, 3])
    True
    """
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    return False

import math
def closest_power_2(x):
    """ Returns the closest power of 2 that is less than x
    >>> closest_power_2(6)
    4
    >>> closest_power_2(32)
    16
    >>> closest_power_2(87)
    64
    >>> closest_power_2(4095)
    2048
    >>> closest_power_2(524290)
    524288
    """
    if 2 ** (int(math.log(x, 2))) == x:
        return 2 ** (int(math.log(x - 1, 2)))
    else:
        return 2 ** (int(math.log(x, 2)))





# Optional, Extra Credit.
def lab03_extra_credit():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-lab03
  """
  okpy_email = "my_examil@berkeley.edu"
  practice_result_code = "xxxx...xxxxx"
  return (okpy_email, practice_result_code)
