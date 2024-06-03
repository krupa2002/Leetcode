class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
 # definning a class
 # defining a method named twosum
 # List[int], target: int -list of integers, target that we want to find
 # len(num) - calculates the length of integer
 # The nested loop iterates over all possible pairs of indices (i, j) such that i < j.
 # for i in range(n - 1): This loop iterates over all indices i from 0 to n-2 (inclusive).
 # for j in range(i + 1, n): This loop iterates over all indices j from i+1 to n-1 (inclusive), ensuring that i < j.
 # if nums[i] + nums[j] == target: This condition checks if the sum of the numbers at indices i and j equals the target.
 # if the condition is met, it returns the indices i and j as a list, indicating the indices of the two numbers that sum up to the target.
