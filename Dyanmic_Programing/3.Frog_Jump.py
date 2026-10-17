# FROG JUMP
#
# "There is a frog on the 1st step of an N stairs long staircase. The frog wants to reach the Nth stair. HEIGHT[i] is the height of the (i+1)th stair. If Frog jumps from ith to jth stair, the energy lost in the jump is given by |HEIGHT[i-1] - HEIGHT[j-1]|. If the Frog is on ith staircase, he can jump either to (i+1)th stair or to (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair."

def minimum_frog_energy(heights):
	if not heights:
		return 0

	energy_two_stairs_back = 0
	energy_one_stair_back = 0

	for index in range(1, len(heights)):
		one_step_jump = energy_one_stair_back + abs(heights[index] - heights[index - 1])
		two_step_jump = float("inf")
		if index > 1:
			two_step_jump = energy_two_stairs_back + abs(heights[index] - heights[index - 2])

		current_energy = min(one_step_jump, two_step_jump)
		energy_two_stairs_back = energy_one_stair_back
		energy_one_stair_back = current_energy

	return energy_one_stair_back


def minimum_frog_energy_tabulation(heights):
	if not heights:
		return 0

	dp = [0] * len(heights)
	for index in range(1, len(heights)):
		dp[index] = dp[index - 1] + abs(heights[index] - heights[index - 1])
		if index > 1:
			two_step_jump = dp[index - 2] + abs(heights[index] - heights[index - 2])
			dp[index] = min(dp[index], two_step_jump)

	return dp[-1]