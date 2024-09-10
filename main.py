# Determine if a tuple can be made into a palindrome by removing exactly one element
import sys
# returns true if pattern is a palindrome, else returns first index where elements do not match
def check_is_palindrome(pattern):
    for i in range(len(pattern) // 2):
        if pattern[i] != pattern[-(i + 1)]:
            return i
    return True


# Returns true or false if a slice is a palindrome
def check_slice_is_palindrome(pattern):
    for i in range(len(pattern) // 2):
        if pattern[i] != pattern[-(i + 1)]:
            return False
    return True


# returns slice without first element that fails palindrome until its corresponding element
def remove_left_index(pattern, index):
    if index == 0:
        return pattern[1:]
    return pattern[index + 1:-index]


# returns inner slice from first index that doesn't match 
# until the right side element that doesn't match, excluded
def remove_right_index(pattern, index):
    return pattern[index:-(index + 1)]


# returns list with middle element removed
def remove_middle_index(pattern):
    del pattern[len(pattern) // 2]
    return pattern


# Fill in find_palindrome
def find_palindrome(pattern):
    if (not isinstance(pattern, tuple)) or (len(pattern) < 3) or (pattern is None):
        return None
    index_or_true = check_is_palindrome(pattern)
    if isinstance(index_or_true, bool):  # if already palindrome
        return tuple(remove_middle_index(list(pattern)))
    else:  # not already palindrome
        if check_slice_is_palindrome(remove_right_index(pattern, index_or_true)):
            if index_or_true == 0:
                return tuple(pattern[:-1])
            return tuple(pattern[:-(index_or_true + 1)] + pattern[-(index_or_true):])
        elif check_slice_is_palindrome(remove_left_index(pattern, index_or_true)):
            return tuple(pattern[:index_or_true] + pattern[index_or_true + 1:])


def main():
    pattern = sys.argv[1:]
    print(find_palindrome(tuple(pattern)))
    return

main()

'''
PSEUDOCODE
MAKE SURE YOU ARE GIVEN A TUPLE

evaluate pattern from left and right checking to see if indexs match

IF any index on left and right doesn't match
THEN 
    check if remaining slice is palindrome with left index removed
    check if remaining slice is palindrome with right index removed
    IF neither slice is a palindrome 
        RETURN NONE
ELSE
    IF palindrome is odd length
        remove middle index 
    RETURN TUPLE
'''
