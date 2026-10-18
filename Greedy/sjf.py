"""
Problem Statement: Shortest Job First (or SJF) CPU Scheduling
--------------------------------------------------------------------------------
Shortest Job First (SJF) is a CPU scheduling policy that selects the waiting
process with the smallest execution (burst) time to execute next.

Given an array of integers `n` representing the burst times of `n` processes arriving
at time 0, calculate the **average waiting time** for all processes.

Note:
- The waiting time of a process is the total time it has to wait in the queue before
  its execution starts.
- Return the integer part (truncated value) of the average waiting time.

Example:
--------
Input:
    n = 5
    bt = [4, 3, 7, 1, 2]  (Burst times for processes P1, P2, P3, P4, P5)

Output:
    4

Explanation:
1. Sort the burst times in ascending order (SJF policy):
   - Sorted burst times: [1, 2, 3, 4, 7] (corresponding to P4, P5, P2, P1, P3)
2. Calculate the waiting time for each process:
   - Process P4 (burst 1): Starts at time 0. Waiting time = 0. Ends at time 1.
   - Process P5 (burst 2): Starts at time 1. Waiting time = 1. Ends at time 3.
   - Process P2 (burst 3): Starts at time 3. Waiting time = 3. Ends at time 6.
   - Process P1 (burst 4): Starts at time 6. Waiting time = 6. Ends at time 10.
   - Process P3 (burst 7): Starts at time 10. Waiting time = 10. Ends at time 17.
3. Total waiting time = 0 + 1 + 3 + 6 + 10 = 20.
4. Average waiting time = Total waiting time / Number of processes = 20 / 5 = 4.


"""

def solve(bt: list[int]) -> int:
    # Sort the burst times to always pick the shortest job first
    bt.sort()

    total_waiting_time = 0
    current_time = 0

    for burst_time in bt:
        # The waiting time for the current process is the time elapsed so far
        total_waiting_time += current_time
        # Increment the current time by this process's burst time
        current_time += burst_time

    # Return the average waiting time (integer division to truncate decimals)
    return total_waiting_time // len(bt)