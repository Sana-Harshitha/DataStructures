# CLIMIBING STAIRS 
# 
# "You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair. Each time you can either climb one step or two steps. You are supposed to return the number of distinct ways in which you can climb from the 0th step to Nth step."


def climb_stairs(number_of_stairs):
	if number_of_stairs < 0:
		raise ValueError("number_of_stairs must be non-negative")
	if number_of_stairs <= 1:
		return 1

	ways_two_steps_back = 1
	ways_one_step_back = 1
	for _ in range(2, number_of_stairs + 1):
		current_ways = ways_one_step_back + ways_two_steps_back
		ways_two_steps_back = ways_one_step_back
		ways_one_step_back = current_ways

	return ways_one_step_back

