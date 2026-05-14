class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we want to read fowards and backwards, so we should have two pointers
        # char.isalnum() returns true if a character is alphanumeric

        # we also could do the cheeky python solution
        # first we make the input string into a single string with only alpha numeric
        # also need to make case insensitive
        new_str = ''.join(char for char in s if char.isalnum())
        new_str = new_str.upper()
        print(new_str)
        if new_str == new_str[::-1]:
            return True
        return False