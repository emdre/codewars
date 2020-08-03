"""Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3"""


def highest_rank(arr):
    dict = {}
    for item in arr:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
    max_val = max(dict.values())
    return max([key for key, val in dict.items() if val == max_val])

