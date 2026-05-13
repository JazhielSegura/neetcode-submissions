class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Intitialize dictionary
        # my_dict = dict()

        # # Iterate over input list
        # for val in nums:
        #     # If the value isn't in dict, initialize it
        #     if val not in my_dict:
        #         my_dict[val] = 1
        #     # If we hit this, we have a duplicate
        #     else:
        #         # my_dict[val] += 1
        #         # Since the question just wants true if any duplicate, return true here
        #         return True
        
        # # After the loop if we get no multi-hits return false
        # return False

        copy = set(nums)

        if len(copy) == len(nums):
            return False
        else:
            return True

        