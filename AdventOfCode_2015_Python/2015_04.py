import doctest
import hashlib

PUZZLE_KEY = "bgvyzdsv"


def main():
    """
    Testing known values given by example:

    >>> get_coin_hash("abcdef", 5)
    609043
    >>> get_coin_hash("pqrstuv", 5)
    1048970
    """
    part_one_key = get_coin_hash(PUZZLE_KEY, 5)
    print("Key for Part 1:", part_one_key)
    part_two_key = get_coin_hash(PUZZLE_KEY, 6)
    print("Key for part 2:", part_two_key)


def get_coin_hash(key, digits):
    key_incrementor = 0
    if test_coin_key(key, digits) == True:
        return key
    while True:
        new_key = key + str(key_incrementor)
        if test_coin_key(new_key, digits) == True:
            return key_incrementor
        else:
            key_incrementor += 1


def test_coin_key(key, digits):
    md5_hash = get_hex_md5_hash(key)
    return test_coin_hash(md5_hash, digits)


def get_hex_md5_hash(key):
    md5_hash = hashlib.md5(key.encode())
    hex_hash = md5_hash.hexdigest()
    return hex_hash


def test_coin_hash(hex_value, digits):
    hex_list = get_hex_list(hex_value, digits)
    int_list = []
    if hex_list_all_ints(hex_list, digits):
        int_list = convert_hex_list_to_int(hex_list)
        if hex_list_all_zeroes(int_list, digits):
            return True
    else:
        return False


def hex_list_all_ints(hex_list, digits):
    int_list = []
    for item in hex_list:
        try:
            int(item)
            int_list.append(int(item))
            if len(int_list) == digits:
                return True
        except ValueError:
            return False


def convert_hex_list_to_int(hex_list):
    return [int(i) for i in hex_list]


def hex_list_all_zeroes(hex_list, digits):
    zero_count = 0
    for hex in hex_list:
        if hex == 0:
            zero_count += 1
            if zero_count == digits:
                return True
        else:
            return False


def get_hex_list(hex_value, digits):
    return [i for i in hex_value[0:digits]]


if  __name__ == "__main__":
    doctest.testmod()
    main()