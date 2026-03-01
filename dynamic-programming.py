# %% [markdown]
# # Dynamic Programming (DP)

# %% [markdown]
# ## Memozation - Top-Down

# %% [markdown]
# Keep tranck of the already calculated/solved ub problem values.

# %%
# recursive fibinnaci calculation
def fib_recursive(n):
    if n <= 2:
        res = 1
    else:
        res = fib_recursive(n - 1) + fib_recursive(n - 2)
    return res

%timeit fib_recursive(10)

# %%
# DP- memozation approach (method 1): Top-down - starting from thelarger problem caching results of each stage
cache = {}

def fib_memoi(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        res = 1
    else:
        res = fib_memoi(n - 1) + fib_memoi(n - 2)
    
    cache[n] = res
    return res

%timeit fib_memoi(10)

# %% [markdown]
# ## Bottom Up - Tabuation
# ```
# In bottom up approach we start from smaller subproblems first and gradually move up to larger problems. 
# We need to solve the dependent sub problemns frst in order to come to a larger problem. Therefor the order of subproblems matter. 
# We have to solve the subproblems in a topological sort order.
# If needed, we can delete unused subproblem results to save space.
# Subproblems must not form a cycle, if so we cannot sorted them in a topological order.
# ```

# %%
# DP- tabulation approach (method 1): Bottom up - solve the smaller problems first

def fib_memoi_2(n):
    memo = {}

    for i in range(1, n + 1):
        if n <= 2:
            fib = 1
        else:
            fib = memo[i - 1] + memo[i - 2]
        
        memo[i] = fib
            
    return memo[n]

%timeit fib_memoi(10)

# %%
%timeit fib_recursive(10)
%timeit %timeit fib_memoi(10)
%timeit %timeit fib_memoi_2(10)

# %% [markdown]
# ### Coin Problem
# 
# https://leetcode.com/problems/coin-change/description/

# %% [markdown]
# #### Recursive non DP Approach

# %%
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        INF = float("inf")
        count = INF
        for c in coins:
            subproblem = amount - c
            sub_count = self.coinChange(coins, subproblem)
            if sub_count != -1:
                count = min(count, sub_count + 1)
        
        return count if count != INF else -1
        

# %% [markdown]
# #### DP with Memoization

# %%
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        INF = float("inf")

        def dp_with_memo(amount):
            if amount == 0: 
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            count = INF

            for c in coins:
                subproblem = amount - c
                sub_count = dp_with_memo(subproblem)
                memo[subproblem] = sub_count
                
                if sub_count != -1:
                    count = min(count, sub_count + 1)
            return count if count != INF else -1
        
        return dp_with_memo(amount)
        


# %% [markdown]
# ## 0/1 Knapsack Problem

# %% [markdown]
# The knapsack problem asks: "Given items with weights and values, what's the maximum value you can fit into a bag with a weight limit?"
# 
# The 0/1 means each item can only be taken once (either you take it or you don't).

# %% [markdown]
# ### Brute Force 0/1 Knapsack — O(2^n)
# 
# The idea is simple: try every possible subset of items, check if it fits within capacity, and track the maximum value.

# %%
def knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    best = 0

    for mask in range(1 << n):          # iterate over all 2^n subsets
        total_weight = 0
        total_value = 0

        for i in range(n):
            if mask & (1 << i):         # if item i is in this subset
                total_weight += weights[i]
                total_value += values[i]

        if total_weight <= capacity:    # only consider valid subsets
            best = max(best, total_value)

    return best


# %% [markdown]
# ```
# ### How the bitmask works
# 
# With `n=3` items, there are `2^3 = 8` possible subsets:
# 
# mask = 000  →  take nothing
# mask = 001  →  take item 0
# mask = 010  →  take item 1
# mask = 011  →  take item 0 and 1
# mask = 100  →  take item 2
# mask = 101  →  take item 0 and 2
# mask = 110  →  take item 1 and 2
# mask = 111  →  take all items
# ```
# 
# mask & (1 << i) checks whether bit i is set — i.e. whether item i is included in this subset.

# %% [markdown]
# ### Recursive version (more intuitive)

# %%
def knapsack_recursive(weights, values, capacity, i=0):
    # base case: no items left or no capacity
    if i == len(weights) or capacity == 0:
        return 0

    # option 1: skip item i
    skip = knapsack_recursive(weights, values, capacity, i + 1)

    # option 2: take item i (only if it fits)
    take = 0
    if weights[i] <= capacity:
        take = values[i] + knapsack_recursive(weights, values, capacity - weights[i], i + 1)

    return max(skip, take)


# %% [markdown]
# ```
# 
# Each call branches into **skip** or **take**, forming a binary tree of depth `n` → **O(2^n)** calls.
#                      (i=0, cap=5)
#                     /            \
#           skip item 0           take item 0
#           (i=1, cap=5)          (i=1, cap=3)
#           /       \              /          \
#     skip i1     take i1     skip i1       take i1
#    (i=2,c=5)  (i=2,c=2)  (i=2,c=3)    (i=2,c=0)
#       ...        ...        ...            ...
# 
# 
# 
# ### Tiny example traced
# 
# weights = [2, 3],  values = [6, 10],  capacity = 5
# 
# 
# knapsack(cap=5, i=0)
# ├── SKIP item0 → knapsack(cap=5, i=1)
# │   ├── SKIP item1 → knapsack(cap=5, i=2) = 0   (no items left)
# │   └── TAKE item1 → 10 + knapsack(cap=2, i=2) = 10 + 0 = 10
# │   → max(0, 10) = 10
# │
# └── TAKE item0 → 6 + knapsack(cap=3, i=1)
#     ├── SKIP item1 → knapsack(cap=3, i=2) = 0
#     └── TAKE item1 → 10 + knapsack(cap=0, i=2) = 10 + 0 = 10
#     → max(0, 10) = 10
#     → 6 + 10 = 16
# 
# Final: max(10, 16) = 16 ✅
# 
# ---
# 
# ### The key mental model
# 
# Think of it as a **decision tree**. Each level = one item. Each branch = skip or take.
# 
#                  start
#                 /     \
#            skip i0    take i0
#             /   \      /    \
#        skip i1 take  skip  take
#                 i1    i1    i1
# ```

# %% [markdown]
# ### DP Solution

# %% [markdown]
# ```
# The recursive thinking was:
# 
# "For item i with remaining capacity w, what's the best value?"
# 
# DP just pre-computes all answers to that question and stores them in an array.
# dp[w] = best value achievable with capacity w
# 
# Instead of going top-down (recursion), we go bottom-up — start from no items, add one item at a time.
# ```

# %%
# 0/1 Knapsack template
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):  # reverse to avoid reuse
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# %%
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# %% [markdown]
# ```
# dp[w]                          # ← this is SKIP  (value without item i)
# dp[w - weights[i]] + values[i] # ← this is TAKE  (value with item i)
# ```
# 
# **It's the exact same skip/take decision as recursion** — just written as an array update instead of a function call.
# 
# ---
# 
# ### Step by step example
# ```
# weights = [2, 3],  values = [6, 10],  capacity = 5
# ```
# 
# **Start:** no items considered yet
# ```
# dp = [0, 0, 0, 0, 0, 0]
#        w=0 1  2  3  4  5
# ```
# 
# ---
# 
# **After item 0** (weight=2, value=6):
# 
# For each `w`, ask: *"skip item0, or take item0?"*
# ```
# w=5: max(dp[5], dp[5-2]+6) = max(0, 0+6) = 6
# w=4: max(dp[4], dp[4-2]+6) = max(0, 0+6) = 6
# w=3: max(dp[3], dp[3-2]+6) = max(0, 0+6) = 6
# w=2: max(dp[2], dp[2-2]+6) = max(0, 0+6) = 6
# w=1: skipped (item weighs 2, can't fit in w=1)
# 
# dp = [0, 0, 6, 6, 6, 6]
# ```
# 
# Reading this: *"with only item0 available, any bag of size ≥2 can hold value 6"* ✅
# 
# ---
# 
# **After item 1** (weight=3, value=10):
# ```
# w=5: max(dp[5], dp[5-3]+10) = max(6, dp[2]+10) = max(6, 6+10) = 16
# w=4: max(dp[4], dp[4-3]+10) = max(6, dp[1]+10) = max(6, 0+10) = 10
# w=3: max(dp[3], dp[3-3]+10) = max(6, dp[0]+10) = max(6, 0+10) = 10
# 
# dp = [0, 0, 6, 10, 10, 16]
# ```

# %% [markdown]
# ## 416. Partition Equal Subset Sum
# 
# https://leetcode.com/problems/partition-equal-subset-sum/description/

# %%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        n = len(nums)
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True  # as empty subset forms sum 0

        for num in nums:
            for t_sum in range(target, num - 1, -1):
                dp[t_sum] = dp[t_sum] or dp[t_sum - num]  # already t_sum can be formed w/o num OR t_sum can be formed using num
        
        return dp[target]

    def canPartition1(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:  # cannot divide into similar sum groups if sum is odd
            return False

        capacity = s // 2
        # turns into a 0/1 knapsack problem with both `weights` and `values` are equal to `nums`

        n = len(nums)
        dp = [0] * (capacity + 1)

        for i in range(n):
            for w in range(capacity, nums[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - nums[i]] + nums[i])
        # print(dp)
        return dp[capacity] == capacity


        

# %% [markdown]
# ## 494. Target Sum
# 
# https://leetcode.com/problems/target-sum/description/

# %%
class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """
        O(2^n)
        """
        count = 0
        def dfs(i, t_sum):
            nonlocal count

            if i == len(nums):
                if t_sum == target:
                    count += 1
                    return True
                return False
            
            add = dfs(i + 1, t_sum + nums[i])
            sub = dfs(i + 1, t_sum - nums[i])

            return add + sub
        dfs(0, 0)
        return count

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        P - positive numbers' sum
        N - negative numbers' sum (abs value)
        P + N = totalSum -- (1)
        P - N = target   -- (2)
        So, 
        2P = (totalSum + target)
        P = (totalSum + target) / 2
        
        - we should find number of subsets (using only positive values) to create exactly P
        """
        total_sum = sum(nums)

        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        P = (total_sum + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1  # one way to reach 0 (empty subset)
        
        for num in nums:
            for c_sum in range(P, num - 1, -1):
                dp[c_sum] += dp[c_sum - num]
        
        return dp[P]


        

# %% [markdown]
# `dp[0] = 1` is crucial — it means *"there's exactly 1 way to reach sum 0 (take nothing)"*, so every time we find `dp[currSum - num]` is reachable, we **add** those ways.
# 
# ### Traced Example
# ```
# nums = [1,1,1,1,1], target = 3
# totalSum = 5
# P = (5+3)/2 = 4
# 
# dp = [1, 0, 0, 0, 0]   ← dp[0]=1
# 
# num=1: dp[1]+=dp[0]=1, dp[2]+=dp[1]... → [1,1,0,0,0]
# num=1: dp[2]+=dp[1]=1, dp[1]+=dp[0]=1  → [1,2,1,0,0]
# num=1:                                  → [1,3,3,1,0]
# num=1:                                  → [1,4,6,4,1]
# num=1:                                  → [1,5,10,10,5]
# 
# dp[4] = 5 ✅
# ```

# %% [markdown]
# ## 322. Coin Change
# 
# https://leetcode.com/problems/coin-change/description/

# %%
def coinChange(coins, amount):
    def dfs(remaining):
        """
        O(amount^n)
        """
        if remaining == 0:  return 0        # done!
        if remaining < 0:   return float('inf')  # overshot
        
        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining - coin)
            min_coins = min(min_coins, result + 1)
        
        return min_coins
    
    ans = dfs(amount)
    return ans if ans != float('inf') else -1

# %% [markdown]
# ```
# 
# This is O(amount^n) — extremely slow, tons of repeated subproblems.
# 
# ---
# 
# ### Step 2: The DP Insight
# 
# Notice: to find min coins for amount `36`, you need min coins for `35`, `31`, `26` (36 minus each coin). Those subproblems overlap massively.
# ```
# dp[a] = minimum coins needed to make amount a
# ```
# 
# For each amount `a`, try every coin and ask:
# > *"If I use this coin, I need `dp[a - coin]` coins for the rest. Is that better?"*
# ```
# dp[a] = min(dp[a - coin] + 1)  for all coins
# 

# %%
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # to form 0 we need 0 coints
        min_count = float("inf")

        for a in range(amount + 1):
            for c in coins: # permutations (all coins are freshly available at each step)
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        """recursion"""
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        INF = float("inf")
        count = INF
        for c in coins:
            subproblem = amount - c
            sub_count = self.coinChange(coins, subproblem)
            if sub_count != -1:
                count = min(count, sub_count + 1)
        
        return count if count != INF else -1
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        """top-down with memoization"""
        memo = {}
        INF = float("inf")

        def dp_with_memo(amount):
            if amount == 0: 
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            count = INF

            for c in coins:
                subproblem = amount - c
                sub_count = dp_with_memo(subproblem)
                memo[subproblem] = sub_count
                
                if sub_count != -1:
                    count = min(count, sub_count + 1)
            return count if count != INF else -1
        
        return dp_with_memo(amount)
        

# %% [markdown]
# for a in range(1, amount + 1):   # forward ✅
# ```
# 
# That's because coins can be used **unlimited times** (unbounded). Going forward means when we compute `dp[10]` using a coin of value `5`, `dp[5]` may already include that same coin — and that's **fine** here!
# 
# | Problem | Loop direction | Why |
# |---|---|---|
# | 0/1 Knapsack | ← reverse | each item used once |
# | Coin Change | → forward | coins reusable |
# 
# ---
# ```
# 
# ### Traced Example
# ```
# coins = [1, 5, 10, 25],  amount = 36  (simplified to amount=11 here)
# 
# dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
#       0   1    2    3    4    5    6    7    8    9   10   11
# 
# a=1:  try coin=1: dp[1] = min(inf, dp[0]+1) = 1
# dp =  [0, 1, inf, inf, inf, inf, ...]
# 
# a=2:  try coin=1: dp[2] = min(inf, dp[1]+1) = 2
# dp =  [0, 1, 2, inf, inf, inf, ...]
# 
# a=5:  try coin=1: dp[5] = min(inf, dp[4]+1) = 4
#       try coin=5: dp[5] = min(4,   dp[0]+1) = 1  ← better!
# dp =  [0, 1, 2, 3, 4, 1, ...]
# 
# a=10: try coin=1:  dp[10] = dp[9]+1  = 5
#       try coin=5:  dp[10] = dp[5]+1  = 2  ← better!
#       try coin=10: dp[10] = dp[0]+1  = 1  ← even better!
# dp =  [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, ...]
# 
# a=11: try coin=1:  dp[11] = dp[10]+1 = 2  ✅
#       try coin=5:  dp[11] = dp[6]+1  = 3
#       try coin=10: dp[11] = dp[1]+1  = 2  (tie)
# 
# dp[11] = 2  (10+1) ✅
# ```
# -------------------------------------------
# 
# ```
# if coin <= a:
#     dp[a] = min(dp[a], dp[a - coin] + 1)
# 
# When `coin <= a`, we're saying:
# > *"I can subtract this coin from `a`, and look up the answer for the remainder `a - coin`"*
# 
# If `coin == a`, that's just a **special case** of `coin <= a` where `a - coin = 0`:
# 
# coin=5, a=5:
# dp[5] = min(dp[5], dp[5-5] + 1)
#       = min(inf,   dp[0]   + 1)
#       = min(inf,   0 + 1)
#       = 1  ✅
# 
# `dp[0] = 0` handles this naturally — it means "I used exactly one coin to cover this amount perfectly."
# 
# ---
# 
# ### What if we only did `coin == a`?
# 
# We'd **miss** most solutions. For example:
# 
# coins = [1, 5],  a = 6
# 
# coin == a would only check: is there a coin worth exactly 6? No → dp[6] = inf ❌
# 
# coin <= a checks:
#   coin=1: dp[6] = dp[5] + 1 = 2  ✅
#   coin=5: dp[6] = dp[1] + 1 = 2  ✅
# ```

# %% [markdown]
# ## 518. Coin Change II
# 
# https://leetcode.com/problems/coin-change-ii/description/

# %%
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to build 0 -> no coins

        for c in coins:  # combinations of coins when coins come in the outer loop
            for a in range(amount + 1):
                if c <= a:
                    dp[a] += dp[a - c]
        
        return dp[amount]
        

# %% [markdown]
# ## 198. House Robber
# 
# https://leetcode.com/problems/house-robber/description/

# %%
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])
        for i in range(2, n):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])

        return max(rob1, rob2)

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


    def rob1(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0
            
            skip = dfs(i + 1)  #  skip ith house
            take = nums[i] + dfs(i + 2)  # rob this house, skip next

            return max(skip, take)
        
        return dfs(0)
        

# %% [markdown]
# ## 213. House Robber II
# 
# https://leetcode.com/problems/house-robber-ii/description/

# %%
class Solution:
    """
    Either rob houses [0,1,2, ... n-2]  (exclude last)
    Or     rob houses [1,2,3, ... n-1]  (exclude first)
    
    One of these two will give the best answer. Why? Because in both cases you're guaranteed to never consider both house 0 and house n-1 together.
    """
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        
        
        def sub_rob(houses):
            n2 = len(houses)

            rob1 = houses[0]  # i - 2
            rob2 = max(rob1, houses[1])  # i - 1

            for i in range(2, n2):
                rob1, rob2 = rob2, max(rob2, rob1 + houses[i])
            
            return max(rob1, rob2)

        return max(
            sub_rob(nums[:-1]),
            sub_rob(nums[1:])
        )        
        

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        
        def sub_rob(houses):
            n2 = len(houses)
            
            dp = [0] * n2
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])

            for i in range(2, n2):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            
            return dp[-1]

        return max(
            sub_rob(nums[:-1]),
            sub_rob(nums[1:])
        )        


# %% [markdown]
# ## 740. Delete and Earn
# 
# https://leetcode.com/problems/delete-and-earn/description/

# %%
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        m = max(nums)
        n = m + 1
        
        counter = {}
        scores = [0] * n
        for num in nums:
            counter[num] = counter.get(num, 0) + num
            scores[num] += num
        
        dp = [0] * n
        dp[0] = scores[0]
        dp[1] = max(dp[0], scores[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + scores[i])
        return dp[-1]
            
        
        

        

# %% [markdown]
# ## 1143. Longest Common Subsequence
# 
# https://leetcode.com/problems/longest-common-subsequence/description/

# %% [markdown]
# #### Step 1: Brute Force Thinking
# ```
# Look at the last character of both strings. Two cases:
# text1[i] == text2[j] → this character is in LCS, move both pointers
# text1[i] != text2[j] → skip one of them, try both, take the max
# ```

# %%
def lcs(text1, text2):
    def dfs(i, j):
        if i == len(text1) or j == len(text2):
            return 0                          # ran out of characters
        
        if text1[i] == text2[j]:
            return 1 + dfs(i+1, j+1)         # match! take it
        else:
            return max(dfs(i+1, j),           # skip text1[i]
                       dfs(i, j+1))           # skip text2[j]
    
    return dfs(0, 0)


# %% [markdown]
# ```
# 
# O(2^(m+n)) — too slow, tons of repeated subproblems.
# 
# ---
# 
# ### Step 2: The DP Insight
# 
# `dfs(i, j)` depends only on `i` and `j` — two variables. So build a **2D table**:
# 
# dp[i][j] = LCS length of text1[0..i] and text2[0..j]
# 
# 
# Same two cases as recursion:
# if text1[i] == text2[j]:
#     dp[i][j] = 1 + dp[i-1][j-1]      # match, take it
# 
# else:
#     dp[i][j] = max(dp[i-1][j],        # skip text1[i]
#                    dp[i][j-1])         # skip text2[j]
# ```

# %%
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]  # extra col/row of 0s as base case (empty string)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],  # skip from text1
                        dp[i][j - 1]    # skip from text2
                    )
        return dp[m][n]

# %% [markdown]
# ## 72. Edit Distance
# 
# https://leetcode.com/problems/edit-distance/description/

# %%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # base cases
        for i in range(m + 1):
            dp[i][0] = i          # delete all
        for j in range(n + 1):
            dp[0][j] = j          # insert all
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]                        # free
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],                 # insert
                                    dp[i-1][j],                  # delete
                                    dp[i-1][j-1])                # replace
        
        return dp[m][n]


