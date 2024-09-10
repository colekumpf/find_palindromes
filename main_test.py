from main import find_palindrome

print(find_palindrome(('n','a','n','a')) == ('n','a','n'))   # INCORRECT IF RIGHT REMOVED FIRST
print(find_palindrome(('n','a','n')) == ('n','n')) 
print(find_palindrome(('a','b','c','a')) == ('a', 'b', 'a'))  # INCORRECT IF RIGHT REMOVED FIRST
print(find_palindrome(('a','b','b','c','a')) == ('a', 'b', 'b', 'a')) 
print(find_palindrome('n') == None) 
print(find_palindrome(('c','i','v','i','c')) == ('c', 'i', 'i', 'c')) 
print(find_palindrome(('a', 1, 2, 2, 1, 'a')) == ('a', 1, 2, 1, 'a')) 
print(find_palindrome(('n','a')) == None) 
print(find_palindrome(('ab','a','a')) == ('a','a')) 
print(find_palindrome(1) == None) 
print(find_palindrome((3, 2, 1, 1, 2, 4, 3)) == (3, 2, 1, 1, 2, 3)) 
print(type(find_palindrome((3, 2, 1, 1, 2, 4, 3))) == tuple) 
print(find_palindrome((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == None) 
print(find_palindrome(('ab','a','ab')) == ('ab', 'ab'))


# AI generated test cases

# MAKE SURE INPUT IS TUPLE
print(find_palindrome((1, 2, 3, 3, 2, 1)) == (1, 2, 3, 2, 1)) 
print(find_palindrome(('a', 'b', 'c')) == None) 
print(find_palindrome((1.1, 2.2, 3.3)) == None) 

# NON TUPLES CASES
print(find_palindrome(([1, 2, 3, 2, 1])) == None) 
print(find_palindrome('111') == None)
print(find_palindrome(('',1,'')) == ('','')) 
print(find_palindrome(('abcba')) == None) 
print(find_palindrome((123)) == None) 

# NON PALINDROME CASES
non_palindrome_cases = [
    (1, 2, 3),
    ('a', 'b', 'c'),
    (1, 2, 2, 3)
]
print(find_palindrome(non_palindrome_cases[0]) == None)
print(find_palindrome(non_palindrome_cases[1]) == None)
print(find_palindrome(non_palindrome_cases[2]) == None)

# CAN FORM PALINDROME CASES
can_form_palindrome_cases = [
    (1, 2, 3, 2, 1),
    (0, 1, 2, 2, 1),
    ('a', 'b', 'a', 'c', 'a', 'b', 'a', 'd'),
    (1, 2, 2, 3, 1)
]
print(find_palindrome(can_form_palindrome_cases[0]) == (1, 2, 2, 1))
print(find_palindrome(can_form_palindrome_cases[1]) == (1, 2, 2, 1))
print(find_palindrome(can_form_palindrome_cases[2]) == ('a', 'b', 'a', 'c', 'a', 'b', 'a'))
print(find_palindrome(can_form_palindrome_cases[3]) == (1, 2, 2, 1))

# ALREADY PALINDROME INPUTS
already_palindrome_cases = [
    (1, 2, 1),
    ('a', 'b', 'b', 'a'),
    (2, 3, 2, 3, 2)
]
print(find_palindrome(already_palindrome_cases[0]) == (1, 1))
print(find_palindrome(already_palindrome_cases[1]) == ('a', 'b', 'a'))
print(find_palindrome(already_palindrome_cases[2]) == (2, 3, 3, 2))

# ADDITIONAL TESTS
print(find_palindrome(('a',)) == None)
print(find_palindrome(['a','a','a']) == None)
print(find_palindrome(('a','b','a')) == ('a','a') and 
  type(find_palindrome(('a','b','a'))) == tuple)
print(find_palindrome(('b','a','a')) == ('a','a'))
print(find_palindrome(('a','a','b')) == ('a','a'))
print(find_palindrome(('3','2','1','0','2','4','3')) == None)
print(find_palindrome(('a', 123, 'a')) == ('a','a'))
print(find_palindrome(('a', 'bc', 'c')) == None)
print(find_palindrome(('a', 'bc', 'a')) == ('a','a'))
print(find_palindrome(("abba", "bc", "abba")) == ('abba', 'abba'))
print(find_palindrome(('s', 'i', 'r', 'i', 'd', 'e', 'm', 'a', 'n', 'd', 'i', 'a', 'm',
        'a', 'm', 'a', 'i', 'd', 'n', 'a', 'm', 'e', 'd', 'i', 'r', 'i', 's'))== 
        ('s', 'i', 'r', 'i', 'd', 'e', 'm', 'a', 'n', 'd', 'i', 'a', 'm', 
         'm', 'a', 'i', 'd', 'n', 'a', 'm', 'e', 'd', 'i', 'r', 'i', 's'))

# LONG PALINDROME TEST CASES
print(find_palindrome((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)) == 
      (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1))
print(find_palindrome(('z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')) ==
         ('z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))
print(find_palindrome((True, False, True, False, True, False, True, False, True, False, 
                       False, True, False, True, False, True, False, True, False, True)) ==
                       (True, False, True, False, True, False, True, False, True, False, 
                        True, False, True, False, True, False, True, False, True))

print(find_palindrome((None)) == None)
print(find_palindrome(1) == None)
print(find_palindrome(('1','2','3','a','3','2','1')) == ('1','2','3','3','2','1'))
print(find_palindrome(('`','.','.','`'))==('`', '.', '`'))