txt = input("enter phrase:\n")
def is_palindrome(text):
    newString = "".join(c for c in text if c.isalpha())
    if newString == newString[::-1]:
        return True
    else:
        return False
    
#is_palindrome('Mr. Owl ate my metal worm') true
    
#is_palindrome('Eva, can I see bees in a cave?') true
    
def is_isogram(text):
    newString = "".join(c for c in text if c.isalpha())
    for x in newString:
        if newString.count(x) > 1:
            return False
    return True
    
    #is_isogram('uncopyrightables') true
    


def is_pangram(text):
    import string
    alphabet = string.ascii_lowercase
    newString = "".join(c for c in text if c.isalpha())
    for char in alphabet:
        if char not in newString:
            return False
    return True
    # is_pangram('The quick brown fox jumps over the lazy dog') true
    

txt1 = input ("enter second phrase:\n")
def is_anagram(text1, text2):
    newString1 = "".join(c for c in text1 if c.isalpha())
    newString2 = "".join(c for c in text2 if c.isalpha())
    for char in newString2:
        if char not in newString1 or len(newString2) != len(newString1):
            return False
    return True

    """
    is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass
