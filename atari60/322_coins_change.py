from typing import List
'''
step1:

dynamic programming
time: O(amount*coins.length)
space: O(amount)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        max_num = amount+1
        coins_minimum = [0] + [max_num for i in range(amount)]
        coins.sort()#for文ないでbreakを使うため
        for num in range(amount+1):
            for coin in coins:
                if num < coin:
                    break
                else:
                    coins_minimum[num] \
                    = min(coins_minimum[num - coin]+1, coins_minimum[num])

        return coins_minimum[amount] if coins_minimum[amount] != max_num else -1


'''
step2:

dynamic programming
time: O(amount*coins.length)
space: O(amount)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        min_num_coins = [0] + [inf for i in range(amount+1)]

        coins.sort()
        for curr_num in range(1, amount+1):
            for coin in coins:
                prev_num = curr_num - coin
                if prev_num < 0:
                    break
                else:
                    min_num_coins[curr_num] = min(min_num_coins[curr_num], min_num_coins[curr_num-coin]+1)
            
        if min_num_coins[amount] == inf :
            return -1
        else:
            return min_num_coins[amount]
