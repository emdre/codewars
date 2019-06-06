"""Given an array of numbers (a list in groovy), determine whether the sum of all of the numbers is odd or even.

Give your answer in string format as 'odd' or 'even'.

If the input array is empty consider it as: [0] (array with a zero)."""


def oddOrEven(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
