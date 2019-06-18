"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""


def kebabize(string):
    result = ""
    for char in string:
        if char.isupper():
            result += "-" + char.lower()
        elif char.isdigit():
            result += ""
        else:            
            result += char
    return result.lstrip("-")
