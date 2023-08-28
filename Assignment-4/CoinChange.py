'''
Given a list of coin denominations and a target sum, return the number of possible ways to make change for that sum.

Input:
Coins: [2, 5, 10]

Sum: 20
Output: 6 (Options are: 10 2s; 4 5s; 2 10s; 
                        5 2s & 2 5s; 
                        5 2s & 1 10; 
                        2 5s & 1 10)

Sum: 15
Output: 3 (Options are: 5 2s & 1 5; 1 5 & 1 10; 3 5s)

Approach: dp
Time complexity:  O(N*K) where N represents the number of coins in the coins array and K represents target
because we iterate through every coin in the coins array and then we also iterate through K times
Space complexity: O(K) because our dp array will store up to target + 1
Time taken: 1hr+

'''
def coinChange(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, target + 1): #dp[i] represents the number of combinations that sum up to i.
            dp[i] += dp[i - coin]

    return dp[-1]

coins = [2, 5, 10]
sum = 20
print(coinChange(coins, sum)) # 6
sum = 15
print(coinChange(coins, sum)) # 3
