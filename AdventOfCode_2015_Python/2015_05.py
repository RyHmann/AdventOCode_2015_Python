import doctest
import re

ALLOWED_VOWELS = ["a","e","i","o","u"]
DISSALLOWED_STRINGS = ["ab","cd","pq","xy"]


def main():
    """
    Testing using known outcomes

    >>> "ugknbfddgicrmopn"
    True
    >>> "aaa"
    True
    >>> "jchzalrnumimnmhp"
    False
    >>> is_naughty("haegwjzuvuyypxyu")
    False
    >>> "dvszwmarrgswjxmb"
    False
    """
    result = has_naughty_string("abcvdqrxy")
    print(result)

    
def has_naughty_string(string):
    is_naughty = []
    for string in DISSALLOWED_STRINGS:
        is_naughty.append(re.compile(string))
    for reg in is_naughty:
        if is_naughty.match(string):
            return True
        else:
            return False

if __name__ == "__main__":
    #doctest.testmod()
    main()