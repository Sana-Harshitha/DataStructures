def rob1(nums):
    prev=0
    prev2=0

    for money in nums:
        curr=max(prev2+money,prev)
        prev2 = prev
        prev=curr
    return prev


def rob(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    case1 = rob1(nums[:-1])  # Exclude last house
    case2 = rob1(nums[1:])   # Exclude first house

    return max(case1, case2)


print(rob([2, 3, 2]))       # 3
print(rob([1, 2, 3, 1]))    # 4
print(rob([1, 2, 3]))       # 3