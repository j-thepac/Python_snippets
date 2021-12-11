"""
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.

In Racket, the function is called palindrome?

(palindrome? "nope") ; returns #f
(palindrome? "Yay")  ; returns #t


"""

def is_palindrome(s):
    s=s.lower()
    return (s==s[::-1])


def sample_tests():
    assert(is_palindrome('a')== True)
    assert(is_palindrome('aba')== True)
    assert(is_palindrome('Abba')== True)
    assert(is_palindrome('malam')== True)
    assert(is_palindrome('walter')== False)
    assert(is_palindrome('kodok')== True)
    assert(is_palindrome('Kasue')== False)


sample_tests()