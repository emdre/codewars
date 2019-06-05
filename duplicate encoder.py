
"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""



def duplicate_encode(word):
    word = list(word.lower())
    new = []
    for char in word:
        count = word.count(char)
        if count == 1:
            new.append("(")
        else:
            new.append(")")
    return ''.join(new)
