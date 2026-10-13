# Imagine a frog trying to climb a staircase with different stair heights, wanting to get from the very first step to the last one. Instead of only being able to jump 1 or 2 steps at a time, the frog can now jump anywhere from 1 up to K steps forward in a single leap. Every time it jumps, it spends energy equal to the height difference between the step it leaves and the step it lands on. Your goal is to figure out the path that costs the least amount of total energy to reach the top.


def minimum_frog_energy_k_jumps(heights, k):
    n = len(heights)
    if n == 0:
        return 0

    dp = [0] * n

    for i in range(1, n):
        dp[i] = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                cost = dp[i - j] + abs(heights[i] - heights[i - j])
                dp[i] = min(dp[i], cost)
    return dp[n - 1]
    
	
