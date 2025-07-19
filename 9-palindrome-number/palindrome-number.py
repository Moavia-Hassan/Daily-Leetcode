class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # First check: Negative numbers are not palindromes.
        # For example, -121 is not considered a palindrome of 121.
        if x < 0:
            return False

        # Second check: Numbers that end in 0 (but are not 0 themselves)
        # cannot be palindromes.
        # For example, 10, 20, 100 cannot be palindromes because their
        # reversed form would be 1, 2, 1, which are different.
        # The exception is 0 itself, which is a palindrome.
        if x % 10 == 0 and x != 0:
            return False

        # If we pass the above checks, we proceed to reverse the number.
        reverted_number = 0
        original_x = x # Keep a copy of the original number for comparison

        while x > 0:
            digit = x % 10          # Get the last digit
            reverted_number = reverted_number * 10 + digit # Append the digit to the reversed number
            x = x// 10                # Remove the last digit from x (integer division)

        # Finally, compare the original number with its reversed counterpart.
        return original_x == reverted_number