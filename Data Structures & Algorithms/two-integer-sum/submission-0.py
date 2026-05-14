class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I think i want ao create a dict with key = num and value = index
        # Then i iterate through list once, updating dict
        # check if target - value is in dict, if so return indices
        # problem says there is guarenteed to be exactly one solution per input
        # if duplicate we just keep first entry in dict, we want shorter index anyways

        my_dict = dict()
        for i in range(len(nums)):
            # We want to check  if the missing number is in the dict
            if (target - nums[i]) in my_dict:
                result = [my_dict.get(target - nums[i]), i]
                return result

            # Add new value: index to dictionary
            if nums[i] not in my_dict:
                my_dict[nums[i]] = i



        