class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same, they are guarenteed not anagrams
        if len(s) != len(t):
            return False

        # dict for s
        dict_s = dict()
        for char in s:
            if char not in dict_s:
                dict_s[char] = 1
            else:
                dict_s[char] += 1

        # dict for t
        dict_t = dict()
        for char in t:
            if char not in dict_t:
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        print(f"dict_s: {dict_s}")
        print(f"dict_t: {dict_t}")

        if dict_s == dict_t:
            return True
        else:
            return False
