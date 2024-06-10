class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sums = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += prefix_sums.get(prefix_sum, 0)
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
        
        return count
