from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        unique_combination = []

        def search_combinations_to_target(index, remaining_target, current_combination):
            if remaining_target == 0:
                unique_combination.append(current_combination)
                return

            if index == len(candidates):
                return

            max_count = remaining_target // candidates[index]

            for count in range(max_count + 1):
                new_combination = current_combination + [
                    candidates[index] for _ in range(count)
                ]
                search_combinations_to_target(
                    index + 1,
                    remaining_target - candidates[index] * count,
                    new_combination,
                )

        search_combinations_to_target(0, target, [])

        return unique_combination
