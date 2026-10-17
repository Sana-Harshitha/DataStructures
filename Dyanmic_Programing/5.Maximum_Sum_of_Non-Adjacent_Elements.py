"""
Problem Statement:   s (House Robber)

Description:
You are given an array of N integers. Your task is to find the maximum sum
of a subsequence such that no two elements in the subsequence are adjacent
in the original array.

In other words, you cannot pick two elements that appear next to each other
(i.e., if you pick the element at index i, you cannot pick the elements at
index i-1 or i+1).

Input Format:
- An integer N, representing the size of the array.
- An array/list of N integers.

Output Format:
- Return a single integer representing the maximum possible sum of a non-adjacent subsequence.

Examples:
- Example 1:
  Input: [1, 2, 4]
  Output: 5
  Explanation: Picking 1 and 4 gives 1 + 4 = 5. Picking 1 & 2 or 2 & 4 is invalid
               because they are adjacent.

- Example 2:
  Input: [2, 1, 4, 9]
  Output: 11
  Explanation: Picking non-adjacent elements 2 and 9 yields 2 + 9 = 11.

Constraints:
- 1 <= N <= 10^5
- -10^4 <= array[i] <= 10^4
"""



def house_robber(nums):
    def helper(i):
        if i >= len(nums):
            return 0

        # Rob the current house
        rob = nums[i] + helper(i + 2)

        # Skip the current house
        skip = helper(i + 1)

        return max(rob, skip)

    return helper(0)


nums = [2, 7, 9, 3, 1]
print(house_robber(nums))  # 12


# SPACE OPTMIZATION
def rob(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        take = nums[i] + dp[i - 2]
        skip = dp[i - 1]

        dp[i] = max(take, skip)

    return dp[n - 1]


print(rob([2, 7, 9, 3, 1]))  # 12
