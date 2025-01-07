# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start = 0
    curr_gas = 0

    for i in range(0, len(gas)):
        current_gain = gas[i]
        curr_gas += current_gain
        curr_gas -= cost[i]

        if curr_gas < 0:
            curr_gas = 0
            start = i + 1
    return start
