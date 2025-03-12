'''
QUESTION AS FOLLOWS -> 
>> PalindromeCreator (str) take the str parameter being passed and determine if it is possible to create a palindromic string of minimum length 3 characters by removing 1 or 2 characters. For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible.
If the input string is already a palindrome, your program should return the string palindrome. Your program should always remove the characters that appear earlier in the string. In the example above, you can also remove ch to form a palindrome but jc appears first, so the correct answer is jc.

The input will only contain lowercase alphabetic characters. Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). The 2 characters you remove do not have to be adjacent in the string.
>> Examples

Input: "mmop" Output: not possible

Input: "kjjjhjjj" Output: k

'''

'''
Step 1: Is it already a palindrome?

The code first checks if the word is already a palindrome. If it is, and it's long enough (at least 3 letters), it says "palindrome".
Step 2: Can we make it a palindrome by taking away one letter?

The code tries taking away each letter one by one and checks if the new word is a palindrome.
If it finds a palindrome, it tells you which letter it took away.
Step 3: Can we make it a palindrome by taking away two letters?

If taking away one letter didn't work, it tries taking away two letters at a time.
If it finds a palindrome, it tells you which two letters it took away.
Step 4: If nothing works, it's "not possible".

If the code tried everything and still couldn't make a palindrome, it says "not possible".
'''

def PalindromeCreator(strParam):
    """
    This function checks if a given string can be made a palindrome by removing one or two characters.

    A palindrome is a word or sentence that reads the same backward as forward, like "racecar".

    Args:
        strParam (str): The input string to check.

    Returns:
        str: 
            - "palindrome" if the input string is already a palindrome (and has at least 3 letters).
            - The character(s) that need to be removed to make the string a palindrome (if possible).
            - "not possible" if the string cannot be made a palindrome by removing one or two characters.
    """

    def isPalindrome(s):
        """
        This helper function checks if a string is a palindrome.

        Args:
            s (str): The string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # We compare the string with its reverse. If they are the same, it's a palindrome!
        return s == s[::-1]

    # 1. Check if the input string is already a palindrome.
    if isPalindrome(strParam) and len(strParam) >= 3:
        # If it is, we say it's a "palindrome".
        return "palindrome"

    # 2. Try removing one character at a time.
    for i in range(len(strParam)):
        # Create a new string by removing the character at position 'i'.
        new_str = strParam[:i] + strParam[i+1:]

        # Check if the new string is a palindrome (and has at least 3 letters).
        if isPalindrome(new_str) and len(new_str) >= 3:
            # If it is, we return the character we removed.
            return strParam[i]

    # 3. Try removing two characters at a time.
    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam)):
            # Create a new string by removing the characters at positions 'i' and 'j'.
            new_str = strParam[:i] + strParam[i+1:j] + strParam[j+1:]

            # Check if the new string is a palindrome (and has at least 3 letters).
            if isPalindrome(new_str) and len(new_str) >= 3:
                # If it is, we return the two characters we removed.
                return strParam[i] + strParam[j]

    # 4. If we couldn't make a palindrome by removing one or two characters, it's "not possible".
    return "not possible"