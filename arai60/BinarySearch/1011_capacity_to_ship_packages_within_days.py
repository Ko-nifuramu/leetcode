"""
BTS

n: weights.length
time: O(days*logn)
space: O(1)
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        min_capacity = max(weights)
        max_capacity = sum(weights)

        ideal_capacity = max_capacity

        while min_capacity < max_capacity:
            capacity = (max_capacity + min_capacity) // 2

            if self.can_ship_within_days(weights, days, capacity):
                ideal_capacity = min(ideal_capacity, capacity)
                max_capacity = capacity
            else:
                min_capacity = capacity + 1

        return ideal_capacity

    def can_ship_within_days(self, weights, days, capacity):
        remain_days = days
        weights_index = 0

        while remain_days > 0:
            shipped_weight = 0

            while weights_index < len(weights):
                if shipped_weight + weights[weights_index] > capacity:
                    shipped_weight -= 1
                    break

                shipped_weight += weights[weights_index]
                weights_index += 1

            remain_days -= 1

            if weights_index - 1 == len(weights) - 1:
                return True

        return False


"""
n: weights.length
d: days

time: O(n*logn)
space: O(1)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship_within_days(capacity):
            loaded_weight = 0
            needed_days = 1

            for weight in weights:
                if loaded_weight + weight <= capacity:
                    loaded_weight += weight
                else:
                    needed_days += 1
                    loaded_weight = weight

            return days >= needed_days

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (high + low) // 2
            if can_ship_within_days(mid):
                high = mid
            else:
                low = mid + 1

        return low
