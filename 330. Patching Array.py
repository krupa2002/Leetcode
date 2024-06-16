class Solution:
    def minPatches(self, nums, n) -> int:
        curr_smallest_not_achieved = 1
        res = 0
        i = 0
        while curr_smallest_not_achieved <= n:
            if i < len(nums) and nums[i] <= curr_smallest_not_achieved:
                curr_smallest_not_achieved += nums[i]
                i += 1
            else:
                # add curr_smallest_not_achieved
                res += 1 
                curr_smallest_not_achieved *= 2
        return res
        
