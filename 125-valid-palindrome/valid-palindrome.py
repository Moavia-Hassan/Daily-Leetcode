class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Convert to lowercase
        s = s.lower()
        
        # Step 2: Remove non-alphanumeric characters
        cleaned_s = ''.join(char for char in s if char.isalnum())
        
        # Step 3: Check if the cleaned string is a palindrome
        return cleaned_s == cleaned_s[::-1]