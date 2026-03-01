# %% [markdown]
# ## 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1913228922/

# %%
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        L, R = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                res[i] = nums[L] ** 2
                L += 1
            else:
                res[i] = nums[R] ** 2
                R -= 1
        return res
        

# %% [markdown]
# ## 46. Permutations
# 
# https://leetcode.com/problems/permutations/description/

# %%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if not x in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        
        backtrack()
        
        return res
        

# %% [markdown]
# ```
# Call backtrack()
# ├─ sol=[], try x=1
# │  ├─ sol=[1], try x=1 → skip (already in sol)
# │  ├─ sol=[1], try x=2
# │  │  ├─ sol=[1,2], try x=1 → skip
# │  │  ├─ sol=[1,2], try x=2 → skip
# │  │  ├─ sol=[1,2], try x=3
# │  │  │  └─ sol=[1,2,3] → len==3, add [1,2,3] to res ✓
# │  │  │  └─ pop 3, sol=[1,2]
# │  │  └─ pop 2, sol=[1]
# │  ├─ sol=[1], try x=3
# │  │  ├─ sol=[1,3], try x=1 → skip
# │  │  ├─ sol=[1,3], try x=2
# │  │  │  └─ sol=[1,3,2] → len==3, add [1,3,2] to res ✓
# │  │  │  └─ pop 2, sol=[1,3]
# │  │  ├─ sol=[1,3], try x=3 → skip
# │  │  └─ pop 3, sol=[1]
# │  └─ pop 1, sol=[]
# │
# ├─ sol=[], try x=2
# │  └─ ... (similar pattern for [2,1,3] and [2,3,1])
# │
# └─ sol=[], try x=3
#    └─ ... (similar pattern for [3,1,2] and [3,2,1])
# 
# ```

# %% [markdown]
# ## 169. Majority Element
# 
# https://leetcode.com/problems/majority-element/description/

# %%
class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
            if counter[num] > n /2:
                return num
    
    def majorityElement(self, nums: List[int]) -> int:
        curr_count = 0
        match = None
        for num in nums:
            if curr_count == 0:
                match = num
            
            curr_count += 1 if num == match else -1
            
        return match

            

            
        
        

# %% [markdown]
# ## 200. Number of Islands
# 
# https://leetcode.com/problems/number-of-islands/description/

# %%
from collections import deque


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        """DFS"""
        h = len(grid)
        w = len(grid[0])

        def cover_island(x, y):
            if x >= h or x < 0 or y >= w or y < 0:
                return

            if grid[x][y] == "1":
                grid[x][y] = "x" # or "0" or anything other than "1"
                
                cover_island(x + 1, y)
                cover_island(x, y + 1)
                cover_island(x - 1, y)
                cover_island(x, y - 1)
                
            else:
                return
            
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    cover_island(i, j)
                    count += 1
        
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count = 0

        for x in range(h):
            for y in range(w):
                if grid[x][y] == "1":
                    count += 1
                    queue = deque([(x, y)])
                    while queue:
                        i, j = queue.popleft()
                        if 0 <= i < h and 0 <= j < w:
                            if grid[i][j] == "1":
                                grid[i][j] = "x" # or "0" or anything other than "1"
                                queue.append((i + 1, j))
                                queue.append((i, j + 1))
                                queue.append((i - 1, j))
                                queue.append((i, j - 1))
        
        return count

        

# %% [markdown]
# ## 100. Same Tree
# 
# https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=depth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False        

# %% [markdown]
# ## 101. Symmetric Tree
# 
# https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=depth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirrorTree(n1: TreeNode, n2:TreeNode):
            if not n1 and not n2:
                return True
            
            if n1 and n2 and n1.val == n2.val:
                return isMirrorTree(n1.left, n2.right) and isMirrorTree(n1.right, n2.left)
            return False
        
        return isMirrorTree(root.left, root.right)
        

# %% [markdown]
# ## 1512. Number of Good Pairs
# 
# https://leetcode.com/problems/number-of-good-pairs/description/

# %%
class Solution:
    def numIdenticalPairs1(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1
        
        return count
        
    
    def numIdenticalPairs2(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        good_pair_count = 0
        # if there are N entries of number X.
        # there are (N-1) + (N-2) + .. + 1 good pairs
        # 1 --> 0
        # 2 --> 1
        # 3 --> 2 + 1 = 3
        # 4 --> 3 + 2 + 1 = 6
        for c in counts.values():
            # good_pair_count += sum([i for i in range(c)])
            good_pair_count += int(c * (c - 1) / 2)
        
        return good_pair_count

    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        good_pair_count = 0
        # if there are N entries of number X.
        # there are (N-1) + (N-2) + .. + 1 good pairs
        # 1 --> 0
        # 2 --> 1
        # 3 --> 2 + 1 = 3
        # 4 --> 3 + 2 + 1 = 6
        for num in nums:
            counts[num] -= 1
            good_pair_count += counts[num]
        
        return good_pair_count

# %% [markdown]
# ## 2558. Take Gifts From the Richest Pile
# 
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

# %%
import heapq

class Solution:
    def pickGifts1(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts = sorted(gifts)
            gifts[-1] = int(gifts[-1] ** 0.5)
        
        return sum(gifts)

    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]

        # heapq._heapify_max(gifts)
        heapq.heapify(gifts)
        for _ in range(k):
            largest = heapq.heappop(gifts)
            # print(largest)
            heapq.heappush(gifts, -int((-largest) ** 0.5))
            # print(gifts)
        return -sum(gifts)


# %%
import heapq
a = [5, 9, 1, 2, 3]
b = [5, 9, 1, 2, 3]
heapq.heapify(a)
heapq._heapify_max(b)
a, b

# %%
heapq.heappop(a), heapq.heappop(b)

# %% [markdown]
# ## 771. Jewels and Stones
# 
# https://leetcode.com/problems/jewels-and-stones/description/

# %%
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # use hash set as the lookup is O(1)
        jewels = set(jewels)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        
        return count

        

# %% [markdown]
# ## 217. Contains Duplicate
# 
# https://leetcode.com/problems/contains-duplicate/description/

# %%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        

# %% [markdown]
# ## 1. Two Sum
# 
# https://leetcode.com/problems/two-sum/description/

# %%
class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        rem_dict = {}
        for i in range(n):
            if nums[i] in rem_dict:
                return [rem_dict[nums[i]], i]
            rem = target - nums[i]
            rem_dict[rem] = i 
            

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        idx_map = {nums[i]: i for i in range(n)}

        for i in range(n):
            rem = target - nums[i]
            if rem in idx_map and idx_map[rem] != i:
                return [idx_map[rem], i]

# %% [markdown]
# ## 1636. Sort Array by Increasing Frequency
# 
# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

# %%
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        counts = sorted(counts.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for num, val in counts:
            res.extend([num] * val)
        return res
        

# %% [markdown]
# ## 70. Climbing Stairs
# 
# https://leetcode.com/problems/climbing-stairs/description/

# %%
from functools import cache


class Solution:
    def climbStairs1(self, n: int) -> int:
        memo = {}

        for i in range(1, n + 1):
            if i == 1:
                count = 1
            elif i == 2:
                count = 2
            else:
                count = memo[i - 1] + memo[i - 2]
            memo[i] = count

        return memo[n]
    
    def climbStairs2(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        
        def findCount(n):
            if n in memo:
                return memo[n]
            count = findCount(n - 1) + findCount(n - 2) 
            memo[n] = count
        
            return memo[n]

        return findCount(n)


    # cache previous function calls - memoization
    @cache
    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_before = 2
        two_before = 1

        for i in range(3, n + 1):
            count = one_before + two_before
            two_before = one_before
            one_before = count

        return count

# %% [markdown]
# ## 64. Minimum Path Sum
# 
# https://leetcode.com/problems/minimum-path-sum/description/

# %%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[m - 1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]

        

# %% [markdown]
# ## 121. Best Time to Buy and Sell Stock
# 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# %%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, (p - buy))
        return profit


# %% [markdown]
# ## 122. Best Time to Buy and Sell Stock II
# 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# %%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            dp = prices[i] - prices[i - 1]
            profit += max(0, dp)
        return profit


# %% [markdown]
# ## 2315. Count Asterisks
# 
# https://leetcode.com/problems/count-asterisks/description/

# %%
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        which_pipe = 0
        for c in s:
            if c == "|":
                which_pipe += 1
                continue
            if which_pipe % 2 == 0 and c == "*":
                count += 1

        return count



# %%
s = "yo|uar|e**|b|e***au|tifu|l"

# %%
import re
re.findall("\|([\w\W]*)\|", s)

# %% [markdown]
# ## 88. Merge Sorted Array
# 
# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp_nums1 = nums1[:m]
        i = 0
        j = 0
        for k in range(m + n):
            if n == 0:
                break
            elif m == 0:
                nums1[:n] = nums2
                break
            if tmp_nums1[i] < nums2[j]:
                nums1[k] = tmp_nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            if i >= m:
                k += 1
                for num2 in  nums2[j:]:
                    nums1[k] = num2
                    k += 1
                break
            if j >= n:
                k += 1
                for num1 in tmp_nums1[i:]:
                    nums1[k] = num1
                    k += 1
                break
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        elif n == 0:
            ...
        else:
            i = m - 1
            j = n - 1
            res_idx = m + n - 1

            while res_idx >= 0:
                if nums1[i] > nums2[j]:
                    nums1[res_idx] = nums1[i]
                    i -= 1
                else:
                    nums1[res_idx] = nums2[j]
                    j -= 1
                res_idx -= 1

                if i < 0 or j < 0:
                    break

            if i >= 0:
                nums1[:res_idx + 1] = nums1[:i + 1]
            elif j >= 0:
                nums1[:res_idx + 1] = nums2[:j + 1]


# %% [markdown]
# ## 27. Remove Element
# 
# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        r = n - 1
        for i in range(n):
            if nums[i] == val:
                while 0 <= r < n and nums[r] == val:
                    r -= 1
                nums[i] = nums[r]
                k += 1
                r -= 1
        
        return n - k
        

# %% [markdown]
# ## 26. Remove Duplicates from Sorted Array
# 
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 1:
            # prev = nums[0]
            res_idx = 1
            for i in range(1, n):
                # if nums[i] != prev:
                if nums[i] != nums[res_idx - 1]:
                    nums[res_idx] = nums[i]
                    # prev = nums[i]
                    res_idx += 1
            
            return res_idx
                


        

# %% [markdown]
# ## 80. Remove Duplicates from Sorted Array II
# 
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        res_idx = 1
        dup_count = 1
        for i in range(1, n):
            if nums[i] != nums[res_idx - 1]:
                nums[res_idx] = nums[i]
                res_idx += 1
                dup_count = 1
            elif dup_count < 2:
                nums[res_idx] = nums[i]
                res_idx += 1
                dup_count += 1
                
        return res_idx


# %% [markdown]
# ## 189. Rotate Array
# 
# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # k == n means we came to the starting position (same array)
        if k > 0:
            for _ in range(k):
                pop_ele = nums[0]
                nums[0] = nums[n - 1]
                for i in range(n - 1):
                    nums[i + 1], pop_ele = pop_ele, nums[i + 1]


    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # k == n means we came to the starting position (same array)
        if k > 0:
            pop_arr = nums[-k:]
            nums[k:] = nums[:-k]
            nums[:k] = pop_arr


    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if k > 0:
            reverse(0, n - 1)
            reverse(0, k - 1)
            reverse(k, n - 1)

        

# %% [markdown]
# ## 55. Jump Game
# 
# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    # fastest O(n)
    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
            
    # dp memoization - very very inefficient O(n^2)
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def find_end(idx):
            # if idx in memo:
            #     return memo[idx]
            # elif idx == n - 1:
            #     memo[idx] = True  
            #     return True
            # elif idx > n - 1:
            #     memo[idx] = False
            #     return False
            # elif nums[idx] == 0:
            #     memo[idx] = False
            #     return False
            if idx >= n - 1:
                return True

            if idx in memo:
                return memo[idx]

            max_j = nums[idx]
            # res = any([find_end(idx + j) for j in range(1, max_j + 1)])
            res = False
            for j in range(1, max_j + 1):
                res = find_end(idx + j)
                if res:
                    break
            memo[idx] = res
            return res
                    
        return find_end(0)

    # dp top-down - O(n^2)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_j = [False] * n
        can_j[n - 1] = True
        
        for i in range(n - 2, -1, -1):
            max_j = nums[i]
            for j in range(1, max_j + 1):
                if i + j < n and can_j[i + j]:
                    can_j[i] = True
                    break
        
        return can_j[0]

# %% [markdown]
# ## 128. Longest Consecutive Sequence
# 
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# %%
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                l = 1
                while num + l in nums_set:
                    l += 1
                max_len = max(max_len, l)
        return max_len
        

# %% [markdown]
# ## 13. Roman to Integer
# 
# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sp_num_map = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        n = len(s)
        res = 0
        idx = 0
        while idx < n:
            if s[idx: idx + 2] in sp_num_map:
                res += sp_num_map[s[idx: idx + 2]]
                idx += 2
            else:
                c = 1
                while idx + c < n and s[idx + c] == s[idx]:
                    c += 1
                res += num_map[s[idx]] * c
                idx += c
        return res
                




        

# %% [markdown]
# ## 58. Length of Last Word
# 
# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        return len(s.strip().split()[-1])
        
    def lengthOfLastWord(self, s: str) -> int:
        curr_len = 0
        space_last = False
        for l in s:
            if l == " ":
                space_last = True
            else:
                if space_last:
                    curr_len = 0
                curr_len += 1
                space_last = False
        return curr_len

# %% [markdown]
# ## 14. Longest Common Prefix
# 
# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        start = strs[0]
        end = strs[-1]
        prefix = []
        for i in range(len(start)):
            if start[i] == end[i]:
                prefix.append(start[i])
            else:
                break
        return "".join(prefix)

        

# %% [markdown]
# ## 28. Find the Index of the First Occurrence in a String
# 
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        nh = len(haystack)

        if nh < n:
            return -1

        for i in range(nh):
            if needle[0] == haystack[i] and needle == haystack[i: i + n]:
                return i
        return -1
        

# %% [markdown]
# ## 392. Is Subsequence
# 
# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        idx_s = 0

        for st in t:
            if st == s[idx_s]:
                idx_s += 1
                if idx_s == n:
                    return True
        return False
        

# %%
ss = ["kdsj13", " skd & 65"]

for s in ss:
    print(s.is)

# %% [markdown]
# ## 125. Valid Palindrome
# 
# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

# %%
import re

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        lower_b = ord("a")
        upper_b = ord("z")
        n_lower_b = ord("0")
        n_upper_b = ord("9")

        while left < right:
            while left < right and not (lower_b <= ord(s[left]) <= upper_b or n_lower_b <= ord(s[left]) <= n_upper_b):
                left += 1
            
            while left < right and not (lower_b <= ord(s[right]) <= upper_b or n_lower_b <= ord(s[right]) <= n_upper_b):
                right -= 1
            
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^A-Za-z0-9]", "", s)
        print(s)

        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


# %% [markdown]
# ## 238. Product of Array Except Self
# 
# https://leetcode.com/problems/product-of-array-except-self/description/

# %%
import numpy as np

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        zero_count = 0
        zero_idx = None
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                zero_idx = i

        if zero_count == 0:
            p = prod(nums)
            return [int(p / num) for num in nums]
            # return [prod(nums[:i]) * prod(nums[i+1:]) for i in range(n)]
        elif zero_count > 1:
            return [0] * n
        else: # zero_count == 1
            res = [0] * n
            res[zero_idx] = prod(nums[:zero_idx]) * prod(nums[zero_idx+1:])
            return res
        
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            res.append(prod(nums[:i]) * prod(nums[i+1:]))
        return res      
    
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_running_prod = [1]
        r_running_prod = [1]
        l_prod = 1
        r_prod = 1
        l_idx = 0
        r_idx = n - 1
        for i in range(n - 1):
            l_prod *= nums[l_idx]
            r_prod *= nums[r_idx]
            l_running_prod.append(l_prod)
            r_running_prod.append(r_prod)
            l_idx += 1
            r_idx -= 1
        
        res = []
        for i in range(n):
            res.append(l_running_prod[i] * r_running_prod[n - 1 - i])
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]
        for i in range(1, n):
            res.append(res[i - 1] * nums[i - 1])

        rp = 1
        for i in range(n - 2, -1, -1):
            rp *= nums[i + 1]
            res[i] *= rp

        return res



# %% [markdown]
# ## 66. Plus One
# 
# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def plusOne1(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = sum([digits[i] * (10 ** (n - i - 1)) for i in range(n)]) + 1
        return [int(x) for x in str(num)]
    
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits

# %% [markdown]
# ## 383. Ransom Note
# 
# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        nr = len(ransomNote)
        nm = len(magazine)

        if nr > nm:
            return False

        m_map = {}
        for s in magazine:
            m_map[s] = m_map.get(s, 0) + 1

        for c in ransomNote:
            if c in m_map and m_map[c] > 0:
                m_map[c] -= 1
            else:
                return False
        
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        nr = len(ransomNote)
        nm = len(magazine)

        if nr > nm:
            return False

        set_r = set(ransomNote)
        set_m = set(magazine)

        if len(set_r) != len(set_m):
            return False



# %% [markdown]
# ## 21. Merge Two Sorted Lists
# 
# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# %%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:return list2
        if not list2: return list1

        if list1.val < list2.val:
            h = ListNode(val=list1.val)
            h1 = list1.next
            h2 = list2
        else:
            h = ListNode(val=list2.val)
            h1 = list1
            h2 = list2.next
        head = h

        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next

        if h1:
            h.next = h1
        else:
            h.next = h2
        
        return head

# %% [markdown]
# ## 104. Maximum Depth of Binary Tree
# 
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        all_paths = []
        stack = [(root, [root.val])]
        max_path_len = 0

        while stack:
            root, path = stack.pop()
            
            if not root.left and not root.right:
                all_paths.append(path)
                max_path_len = max(max_path_len, len(path))
                # print(path)

            if root.left:
                stack.append((root.left, path + [root.left.val]))

            if root.right:
                stack.append((root.right, path + [root.right.val]))
        # print(all_paths)
        return max_path_len


    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all_paths = []
        max_path_len = 0

        def dfs(node: TreeNode, path: List[int]):
            nonlocal max_path_len
            path = path + [node.val]

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)

            if not node.right and not node.left:
                all_paths.append(path)
                max_path_len = max(max_path_len, len(path))
                # print(path)
                return
        
        dfs(root, [])
        # print(all_paths)

        return max_path_len

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all_paths = []
        max_path_len = 0

        def dfs(node: TreeNode, path):
            nonlocal max_path_len
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                all_paths.append(path[:])
                max_path_len = max(max_path_len, len(path))
                # print(path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)
                
            path.pop()
        
        dfs(root, [])
        # print(all_paths)
        return max_path_len

    

# %% [markdown]
# ## 219. Contains Duplicate II
# 
# https://leetcode.com/problems/contains-duplicate-ii/submissions/1922246258/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        idx_track = {}
        n = len(nums)
        if n == 1:
            return False
        for i in range(n):
            if nums[i] in idx_track and (i - idx_track[nums[i]]) <= k:
                return True
            
            idx_track[nums[i]] = i
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        n = len(nums)

        for i in range(n):
            if i > k:
                w.remove(nums[i - k - 1])
            
            if nums[i] in w:
                return True

            w.add(nums[i])
        
        return False
        

# %%
s = set()

# %%
s = s.union(set([1,3,1,4]))
s = s.union(set([1,3,1,4,5,7,2,9]))
s

# %% [markdown]
# ## 269. Alien Dictionary
# 
# https://leetcode.com/problems/alien-dictionary/description/

# %%
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        deps = []
        deps_map = {}
        deps_count = {}
        alphabet = set(words[0])
        nw = len(words)

        for i in range(nw - 1):
            w1 = words[i]
            w2 = words[i + 1]

            alphabet = alphabet.union(set(w2))

            k = 0
            lw1 = len(w1)
            lw2 = len(w2)
            min_l = min(lw1, lw2)
            print(len(w1[k]), len(w2[k]), len(w1[k]) > len(w2[k]))
            
            while k < min_l and w1[k] == w2[k]:
                print(w1[k], w2[k])
                k += 1
            if k == lw2 and lw1 != lw2:
                return ""

            if (lw1==lw2 and lw1==0) or (lw1 != lw2) or (lw1==lw2 and k == 0):
                print(w1, w2, k, ">>>")
                deps.append((w2[k], w1[k]))
            
                if w2[k] not in deps_count:
                    deps_count[w2[k]] = 0

                deps_count[w2[k]] = deps_count[w2[k]] + 1
                
                if w1[k] not in deps_map:
                    deps_map[w1[k]] = []
                
                deps_map[w1[k]].append(w2[k])
        
        for c in alphabet:
            if c not in deps_count:
                deps_count[c] = 0
        
        print(deps)
        print(deps_map)
        print(deps_count)
        
        # alphabet = list(deps_count.keys())
        print(alphabet)
        stack = []
        for c in alphabet:
            if deps_count[c] == 0:
                stack.append(c)
        order = []
        while stack:
            c = stack.pop()
            order.append(c)
            print(deps_map, c)

            for d in deps_map.get(c, []):
                deps_count[d] -= 1
                if deps_count[d] == 0:
                    stack.append(d)
        
        return "".join(order)


# %%
[1, 2] < [1, 3], [1, 3, 3] < [1, 3, 2], \
    ["a", "c"] < ["a", "b"], ["a", "b"] < ["a", "c"], ["a", "b"] == ["a", "b"]

# %%
a = "hlabcdefgijkmnopqrstuvwxyz"
[i for i in map(a.index, "hello")]

# %% [markdown]
# ## 953. Verifying an Alien Dictionary
# 
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

# %%
class Solution:
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order):
            order_map[c] = i
        
        n = len(words)
        if n == 1: return True

        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]
            lw1 = len(w1)
            lw2 = len(w2)
            min_l = min(lw1, lw2)
            k = 0
            while k < min_l:
                if w1[k] == w2[k]:
                    k += 1
                    continue

                if order_map[w1[k]] < order_map[w2[k]]:
                    break
                return False
            else: # one word is the prefix of another (ex: apple, app)
                if lw1 > lw2:
                    return False
        return True
    
    # being short does not always gaurantee fatser execution
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order):
            order_map[c] = i
        n = len(words)

        words = [[order_map[c] for c in w] for w in words]
        return all([words[i] <= words[i + 1] for i in range(n - 1)])


# %% [markdown]
# ## 1768. Merge Strings Alternately
# 
# https://leetcode.com/problems/merge-strings-alternately/description/

# %%
class Solution:
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        n1 = len(word1)
        n2 = len(word2)
        res = []
        while p1 < n1 and p2 < n2:
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1

        if p1 < n1:
            return "".join(res) + word1[p1:]
        return "".join(res) + word2[p2:]
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for c1, c2 in zip(word1, word2):
            res.append(c1 + c2)
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])

        return "".join(res)

# %% [markdown]
# ## 39. Combination Sum
# 
# https://leetcode.com/problems/combination-sum/description/

# %%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        if candidates[0] > target:
            return []
        c_set = set(candidates)
        n = len(candidates)
        res = []
        res_set = set()
        def sub(target, sub_res):
            if target < candidates[0]:
                return None
            
            if target in c_set:
                r = sorted(sub_res + [target])
                rs = "".join(map(str, r))
                if rs not in res_set:
                    res.append(r)
                    res_set.add(rs)

            i = 0
            while i < n and candidates[i] < target:
                i += 1
            
            for i in range(i):
                r = sub(target - candidates[i], sub_res + [candidates[i]])
                if r:
                    rs = "".join(map(str, r))
                    if rs not in res_set:
                        res.append(r)
                        res_set.add(rs)
        
        sub(target, [])
        return res


# %% [markdown]
# ## 1716. Calculate Money in Leetcode Bank
# 
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

# %%
class Solution:
    def totalMoney(self, n: int) -> int:
        nw = int(n / 7)
        rem = n % 7
        print(nw, rem)
        sum = 0

        for i in range(1, nw + 1):
            sum += int((7 / 2) * (i + i + 6))
        
        if rem > 0:
            sum += int((rem / 2) * (nw + 1 + nw + rem))

        return sum


# %%
import heapq

l = [(6, "abdg"), (1, "kdsb"), (5, "akhb")]
heapq.heapify(l)
heapq.heappop(l), heapq.heappop(l), heapq.heappop(l)

# %% [markdown]
# ## 23. Merge k Sorted Lists
# 
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# %%
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        
        if k == 1:
            if lists[0]:
                return lists[0]
            return None
        curr_heads = [(lists[i].val, i, lists[i]) for i in range(k) if lists[i]]  # i added to avaid ties (tie breaker) in the 1st value (as ListNode s cannot be compared)
        heapq.heapify(curr_heads)
        prev = None
        head = None
        while curr_heads:
            val, i, node = heapq.heappop(curr_heads)
            if node.next:
                heapq.heappush(curr_heads, (node.next.val, i, node.next))
            if prev is not None:
                prev.next = node
            else:
                head = node
            prev = node
        return head


# %% [markdown]
# ## 228. Summary Ranges
# 
# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n ==0:
            return []
        
        res = []
        start = nums[0]
        end = nums[0]
        for i in range(1, n):
            if nums[i] > end + 1:
                res.append(f"{end}" if start == end else f"{start}->{end}")
                start = nums[i]
            end = nums[i]
        res.append(f"{end}" if start == end else f"{start}->{end}")
        return res
        


# %%
curr_w = ""
curr_w += "hi"
curr_w

# %% [markdown]
# ## 151. Reverse Words in a String
# 
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        curr_w = ""
        for c in s:
            if c == " ":
                if curr_w:
                    res = f"{curr_w} {res}" if res else curr_w
                curr_w = ""
            else:
                curr_w += c
        if curr_w:
            res = f"{curr_w} {res}" if res else curr_w
        return res

    def reverseWords2(self, s: str) -> str:
        curr_w = ""
        words = []
        for c in s:
            if c == " ":
                if curr_w:
                    words.append(curr_w)
                curr_w = ""
            else:
                curr_w += c
        if curr_w:
            words.append(curr_w)
        return " ".join(words[::-1])

    def reverseWords1(self, s: str) -> str:
        res = ""
        curr_w = ""
        words = []
        for c in s:
            if c == " ":
                if curr_w:
                    words.append(curr_w)
                curr_w = ""
            else:
                curr_w += c
        if curr_w:
            words.append(curr_w)
        
        for i in range(len(words) - 1, -1, -1):
            res += words[i]
            if i > 0:
                res += " "
        return res


        

# %% [markdown]
# ## 9. Palindrome Number
# 
# https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x

    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False

        x= str(x)
        l = 0
        r = len(x) - 1

        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True


# %% [markdown]
# ## 20. Valid Parentheses
# 
# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def isValid(self, s: str) -> bool:
        end_pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in end_pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                start = stack.pop()
                if end_pairs.get(start, None) != c:
                    return False
        if stack:
            return False
        return True
        

# %% [markdown]
# ## 208. Implement Trie (Prefix Tree)
# 
# 

# %%
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie1:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if not curr.is_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["*"] = False

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        if "*" not in curr:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# %% [markdown]
# ## dfgdf

# %%
class Node:
    def __init__(self, children={}):
        self.children = children
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c != "." and c not in curr.children:
                return False
            if c == ".":
                res = []
                for child in curr.children:
                    sub_trie = WordDictionary()
                    sub_trie.root = child
                    res.append(sub_trie.search(word[i + 1:]))
                return any(res)
            curr = curr.children[c]
        if curr.is_end:
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# %%
"jvhsdvjs".startswith("jvh"), "jvhsdvjs".startswith("jvhe")

# %%
[c if c != "." else "*" for c in "ksdb..sd."]

# %%
import re

# %%
words = ["bad", "dad", "mad"]
search = ["pad", "bad", ".ad", "b.."]

for w in words:
    print(1, w, re.findall(f'^.ad$', w))
    print(2, w, re.findall(f'^b..$', w))
    print(3, w, re.findall(f'^b.$', w))
    print(4, w, re.findall(f'^.$', w))

# %% [markdown]
# ## 211. Design Add and Search Words Data Structure
# 
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/?envType=study-plan-v2&envId=top-interview-150

# %%
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary1:

    def __init__(self):
        self.root = Node()
        print("root", self.root.children)

    def addWord(self, word: str) -> None:
        print(f"Adding {word}---")
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            print(c, curr, curr.children)
            if c != "." and c not in curr.children:
                return False
            if c == ".":
                res = []
                for child in curr.children:
                    print("-----------")
                    sub_trie = WordDictionary()
                    sub_trie.root = curr.children[child]
                    res.append(sub_trie.search(word[i + 1:]))
                return any(res)
            curr = curr.children[c]
        if curr.is_end:
            return True
        return False

import re
import heapq

class WordDictionary2:

    def __init__(self):
        self.words = []
        # heapq.heapify(self.words)

    def addWord(self, word: str) -> None:
        # heapq.heappush(self.words, word)
        self.words.append(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if re.findall(f"^{word}$", w):
                print(word, w)
                return True
        return False

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False 

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for i, c in enumerate(word):
            if c == ".":
                for child in curr.children:
                    if curr.children[child].search(word[i + 1:]):
                        return True
                return False
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# %% [markdown]
# ## 107. Binary Tree Level Order Traversal II
# 
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res[::-1]

        

# %% [markdown]
# ## 103. Binary Tree Zigzag Level Order Traversal
# 
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []    

        level_id = 0
        queue = [root]
        res = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_id % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            level_id += 1

        return res
    

# %% [markdown]
# ## 111. Minimum Depth of Binary Tree
# 
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_depth = float(inf)
        queue = [root]
        level_id = 0
        while queue:
            level_id += 1

            for _ in range(len(queue)):
                node = queue.pop(0)
                
                # the 1st left node at level traversal is one of the min depth nodes 
                if not node.left and not node.right:
                    return level_id

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return level_id


    def minDepth3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]
        min_depth = float("inf")
        # all_paths = []

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                min_depth = min(min_depth, len(path))
                # all_paths.append(path)
            
            if node.left:
                stack.append((node.left, path + [node.left]))

            if node.right:
                stack.append((node.right, path + [node.right]))
        
        # print(all_paths)
        # print(min_depth)
        return min_depth

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        min_depth = float(inf)
        
        def dfs(node, path):
            nonlocal min_depth
            path = path + [node.val]
            if not node.left and not node.right:
                min_depth = min(min_depth, len(path))
                return
            
            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)
        
        dfs(root, [])
        return min_depth

    def minDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        min_depth = float(inf)
        def dfs(node, path):
            nonlocal min_depth

            path.append(node.val)

            if not node.left and not node.right:
                min_depth = min(min_depth, len(path))
                
            if node.left:
                dfs(node.left, path)
            
            if node.right:
                dfs(node.right, path)

            path.pop()
        
        dfs(root, [])
        return min_depth
        

# %% [markdown]
# ## 116. Populating Next Right Pointers in Each Node
# 
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = [root]
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                if prev:
                    prev.next = node
                prev = node
                
                # since a complete BST, no need to check for both children
                if node.left: 
                    queue.append(node.left)
                    queue.append(node.right)

        return root
        

# %% [markdown]
# ## 117. Populating Next Right Pointers in Each Node II
# 
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = [root]
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.pop(0)

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
        

# %%
w1 = "hot"
w2 = "bot"

sum(c1!=c2 for c1, c2 in zip(w1, w2)), ord("z"), chr(ord("z"))

# %% [markdown]
# ## 127. Word Ladder
# 
# https://leetcode.com/problems/word-ladder/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
"""
The question asked about the shortest path from beginWord to endWord. Basically we should us a shortest path algorithm like BFS. 
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = [beginWord]
        count = 1
        visited = set([beginWord])
        a_idx = ord("a")
        z_idx = ord("z")
        while queue:
            for _ in range(len(queue)): # separate each level of the search
                word = queue.pop(0)
                # we check for available words by changing a single character of the current word.
                # we check all possibilites by changing from first character to the last character.
                # as there are only 26 different characters, this nested loops are not very costly
                for i in range(len(word)): 
                    for n in range(a_idx, z_idx + 1):
                        new_word = f"{word[:i]}{chr(n)}{word[i+1:]}"
                        if new_word not in visited and new_word in wordSet:
                            queue.append(new_word)
                            visited.add(new_word)
            count += 1
            if endWord in visited:
                return count
        return 0
    
            

# %% [markdown]
# ## 126. Word Ladder II
# 
# https://leetcode.com/problems/word-ladder-ii/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        all_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        parents = defaultdict(set)
        found = False

        current_level = {beginWord}   # track current frontier as a set
        visited = {beginWord}

        while current_level and not found:
            next_level = set()         # collect ALL next-level words first

            for word in current_level:
                for i in range(len(word)):
                    for c in all_letters:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word != word and new_word in wordSet and new_word not in visited:
                            next_level.add(new_word)
                            parents[new_word].add(word)  # multiple parents allowed!

            # Only mark visited AFTER full level is processed
            visited |= next_level

            if endWord in next_level:
                found = True

            current_level = next_level

        if not found:
            return []

        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        return res

    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        visited = set([beginWord])
        queue = deque([beginWord])
        all_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        parents = defaultdict(set)
        found = False
        
        while queue and not found:
            new_nodes = set()
            for _ in range(len(queue)):
                # word = queue.pop(0)
                word = queue.popleft()
                for i in range(len(word)):
                    for c in all_letters:
                        new_word = word[: i] + c + word[i + 1:]
                        if new_word != word and new_word in wordSet and new_word not in visited:
                            queue.append(new_word)
                            new_nodes.add(new_word)
                            parents[new_word].add(word)

            visited |= new_nodes
            if endWord in visited:
                found = True
        if not found:
            return []

        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()
        
        dfs(endWord, [endWord])
        return res

        

# %% [markdown]
# ## 130. Surrounded Regions
# 
# https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        Q = deque()

        for i in range(m):
            if board[i][0] == "O":
                Q.append((i, 0))
            if board[i][n - 1] == "O":
                Q.append((i, n - 1))

        for i in range(n):
            if board[0][i] == "O":
                Q.append((0, i))
            if board[m - 1][i] == "O":
                Q.append((m - 1, i))

        while Q:
            (i, j) = Q.popleft()
            
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == "O": 
                    board[i][j] = "#"

                    Q.append((i + 1, j))
                    Q.append((i - 1, j))
                    Q.append((i, j + 1))
                    Q.append((i, j - 1))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"



    def solve1(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        k = 1
        queue = deque()
        X_set = set()
        O_set = set()

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    queue.append((x, y))
                    surrounded = True
                    
                    while queue:
                        i, j = queue.popleft()
                        if 0 <= i < m and 0 <= j < n:
                            if board[i][j] == "O":
                                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                                    surrounded = False
                                board[i][j] = k

                                queue.append((i + 1, j))
                                queue.append((i - 1, j))
                                queue.append((i, j + 1))
                                queue.append((i, j - 1))

                    if surrounded:
                        X_set.add(k)
                    else:
                        O_set.add(k)
                    k += 1

        for x in range(m):
            for y in range(n):
                if board[x][y] in X_set:
                    board[x][y] = "X"
                elif board[x][y] in O_set:
                    board[x][y] = "O"


# %% [markdown]
# ## 199. Binary Tree Right Side View
# 
# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        right_nodes = []

        while q:
            # level = []
            for _ in range(len(q)):
                node = q.popleft()
                # level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        
            # right_nodes.append(level[-1])
            right_nodes.append(node.val)
        
        return right_nodes

        

# %% [markdown]
# ## 207. Course Schedule
# 
# https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=breadth-first-search

# %%
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        dep_list = [0] * numCourses
        for child, parent in prerequisites:
            prereq_map[parent].append(child)
            dep_list[child] += 1

        queue = deque()
        for i in range(numCourses):
            if dep_list[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            if course in prereq_map:
                for child in prereq_map[course]:
                    dep_list[child] -= 1
                    if dep_list[child] == 0:
                        queue.append(child)
        
        return len(res) == numCourses



        


        

# %% [markdown]
# ## 301. Remove Invalid Parentheses
# 
# https://leetcode.com/problems/remove-invalid-parentheses/submissions/1930745534/?envType=problem-list-v2&envId=breadth-first-search

# %%
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            i= 0
            ctr = 0
            while i<len(s):
                if s[i]== '(':
                    ctr += 1
                elif s[i] == ")":
                    if ctr == 0:
                        return False
                    ctr -= 1
                
                i +=1
            
            return ctr == 0
        
        level ={s}
        while True:
            valid = list(filter(isValid, level))
            print(valid)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for i in range(len(s)) for s in level}
        

# %% [markdown]
# ## 695. Max Area of Island
# 
# https://leetcode.com/problems/max-area-of-island/

# %%
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    area = 0
                    queue.append((x, y))
                    while queue:
                        i, j = queue.popleft()
                        if 0 <= i < m and 0 <= j < n:
                            if grid[i][j] == 1:
                                area += 1
                                grid[i][j] = 0

                                queue.append((i + 1, j))
                                queue.append((i - 1, j))
                                queue.append((i, j + 1))
                                queue.append((i, j - 1))
                    max_area = max(max_area, area)
        return max_area


                

# %% [markdown]
# ## 133. Clone Graph
# 
# https://leetcode.com/problems/clone-graph/

# %%
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = deque([node])
        visited = {node.val: Node(node.val, [])}
        
        while queue:
            curr_node = queue.popleft()
            new_node = visited[curr_node.val]

            for neighbor in curr_node.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                new_node.neighbors.append(visited[neighbor.val])

        return visited[node.val]



# %% [markdown]
# ## 994. Rotting Oranges
# 
# https://leetcode.com/problems/rotting-oranges/

# %%
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh_count = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        if fresh_count == 0:
            return 0
        elif not queue:
            return -1
        step = 0

        while queue:
            rottened = False
            for _ in range(len(queue)): # traverse through each time step/ level
                (x, y) = queue.popleft()
                for (i, j) in [(x + 1, y), (x -1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_count -= 1
                        rottened = True
                        queue.append((i, j))
            
            if rottened:
                step += 1
            else:
                if fresh_count == 0:
                    return step
                return -1
        return step



    def orangesRotting1(self, grid: List[List[int]]) -> int:
        def are_fresh():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return True
            return False

        def get_all_rotten():
            res = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        res.append((i, j))
            return res  

        m = len(grid)
        n = len(grid[0])
        queue = deque(get_all_rotten())
        steps = 0
        
        while queue:
            rottened = False
            for _ in range(len(queue)): # identify levels/time steps
                x, y = queue.popleft()
                for (ii, jj) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        rottened = True
                        queue.append((ii, jj))
            if rottened:
                steps += 1
            else:
                if are_fresh():
                    return -1
                return steps

        if are_fresh():
            return -1
        return steps 


# %% [markdown]
# ## 542. 01 Matrix
# 
# https://leetcode.com/problems/01-matrix/

# %%
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        A reverse method.
        start from 0 points and keep on marking the distances to adjacent cells step by step.
        keep on polulating the distance matrix from 0 to up untill all cells are covered.
        0 -> 1 cells
        1 -> 2 cells etc.
        """
        m = len(mat)
        n = len(mat[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        num = 1
        while q:
            for _ in range(len(q)): # iterate over each distance level upwards
                (x, y) = q.popleft()
                for (ii, jj) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= ii < m and 0 <= jj < n and mat[ii][jj] == -1:
                        mat[ii][jj] = num
                        q.append((ii, jj))
            num += 1
        
        return mat


    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        """
        A reverse method.
        start from 0 points and keep on marking the distances to adjacent cells step by step.
        keep on polulating the distance matrix from 0 to up untill all cells are covered.
        0 -> 1 cells
        1 -> 2 cells etc.
        """
        m = len(mat)
        n = len(mat[0])
        res = [[float(inf)] * n for _ in range(m)]

        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))
                    visited.add((i, j))

        all_ele = m * n
        num = 1
        while len(visited) < all_ele:
            while q:
                for _ in range(len(q)): # iterate over each distance level upwards
                    (x, y) = q.popleft()
                    for (ii, jj) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= ii < m and 0 <= jj < n and ((ii, jj) not in visited):
                            res[ii][jj] = num
                            q.append((ii, jj))
                            visited.add((ii, jj))
                num += 1
        return res


    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        """
        find distance to each cell independently. Inefficient due to many overlapping recalculations
        """
        m = len(mat)
        n = len(mat[0])
        res = mat
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    queue = deque([(i, j)])
                    dist = 1
                    found = False
                    while queue:
                        for _ in range(len(queue)):
                            (x, y) = queue.popleft()
                            for (ii, jj) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                                if 0 <= ii < m and 0 <= jj < n:
                                    if mat[ii][jj] == 0:
                                        found = True
                                    else: # elif mat[ii][jj] == 1 -> else is always 1 as a binary mat 
                                        queue.append((ii, jj))
                        if found:
                            res[i][j] = dist
                            break
                        else:    
                            dist += 1
        return res



# %% [markdown]
# ## 547. Number of Provinces
# 
# https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=graph-theory

# %%
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(city):
            for c in range(n):
                if isConnected[city][c] == 1 and c not in visited:
                    visited.add(c)
                    dfs(c)
        
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                count += 1
        
        return count
                

    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        np = 0
        
        for i in range(n):
            if i in visited:
                continue
            np += 1
            q = deque([i])
            visited.add(i)
            while q:
                city = q.popleft()
                row = isConnected[city]
                for c_city in range(n):
                    if row[c_city] == 1 and c_city != city and (c_city not in visited):
                        visited.add(c_city)
                        q.append(c_city)
        return np




        

# %% [markdown]
# ## 1492. The kth Factor of n
# 
# https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

# %%
from collections import deque

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n == 1:
            factors = [1]
        else:
            factors = []
            n_sqrt = int(n ** 0.5)
            for i in range(1, n_sqrt + 1):
                if n % i == 0:
                    factors.append(i)
            
            for i in range(n_sqrt + 1, n + 1):
                if n % i == 0:
                    factors.append(i)
        if len(factors) < k:
            return -1
        return factors[k - 1]

    def kthFactor2(self, n: int, k: int) -> int:
        if n == 1:
            factors = [1]
        else:
            factors = []
            factors2 = []
            n_sqrt = int(n ** 0.5)
            for i in range(1, n_sqrt + 1):
                if n % i == 0:
                    factors.append(i)
                    ii = n // i
                    if ii != i:
                        factors2.append(ii)
                    print(i, n // i)
            factors.extend(factors2[::-1])
            print(factors)
            print(factors2)
        if len(factors) < k:
            return -1
        return factors[k - 1]


    def kthFactor1(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        if len(factors) < k:
            return -1
        return factors[k - 1]
        

# %% [markdown]
# ## 2405. Optimal Partition of String
# 
# https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

# %%
class Solution:
    def partitionString(self, s: str) -> int:
        c_set = set()
        # s_list = []
        # curr_s = []
        count = 0
        for c in s:
            if c in c_set:
                # s_list.append("".join(curr_s))
                # curr_s = [c]
                c_set = set([c])
                count += 1
            else:
                # curr_s.append(c)
                c_set.add(c)
        # if curr_s:
        if c_set:
            count += 1
            # s_list.append("".join(curr_s))
        
        # return len(s_list)
        return count


# %% [markdown]
# ## 310. Minimum Height Trees
# 
# https://leetcode.com/problems/minimum-height-trees/?envType=problem-list-v2&envId=graph

# %%
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        we can have at most 2 MHTs.
        https://leetcode.com/problems/minimum-height-trees/solutions/5060930/full-explanation-bfs-remove-leaf-nodes-b-4x00
        so what we do is we keep on pruning the leaves (i.e. that have only one connection/edge) until we remain 1, 2 nodes.
        """
        if n == 1:
            return [0]

        child_map = defaultdict(set)
        deps = [0] * n
        for a, b in edges:
            child_map[a].add(b)
            child_map[b].add(a)
            deps[a] += 1
            deps[b] += 1

        leaves_queue = deque([node for node in range(n) if deps[node] == 1])
        node_count = n

        while node_count > 2: # we can only have at most 2 MHTs 
            node_count -= len(leaves_queue)
            for _ in range(len(leaves_queue)):
                leave = leaves_queue.popleft()
                for nebr in child_map[leave]:
                    deps[nebr] -= 1
                    if deps[nebr] == 1:
                        leaves_queue.append(nebr)
        return list(leaves_queue)


    
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Inefficient - bruteforce way
        """
        child_map = defaultdict(set)
        for (a, b) in edges:
            child_map[a].add(b)        
            child_map[b].add(a)

        print(child_map)  
        min_depth = n
        depths = {}
        for node in range(n):
            visited = set()
            queue = deque([node])
            height = 0
            while queue:
                for _ in range(len(queue)): # each level
                    curr_node = queue.popleft()
                    visited.add(curr_node)
                    for child in child_map[curr_node]:
                        queue.append(child)
                if len(visited) == n:
                    depths[node] = height
                    min_depth = min(min_depth, height)
                    break
                height += 1
        print(depths)
        
        return [k for k in depths if depths[k] == min_depth]


# %% [markdown]
# ## 48. Rotate Image
# 
# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1: flip up down
        # step two flip over the main diagonal
        n = len(matrix)
        
        if n > 1:
            for i in range(n // 2):
                for j in range(n):
                    matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        

# %% [markdown]
# ## 73. Set Matrix Zeroes
# 
# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # space O(1)
        # time O(m.n.max(m,n))

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "#"
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "#"
        # print(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False        
        first_col_has_zero = False

        # check if the first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # use the first row and column as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # set the marked rows to zero
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # set the marked columns to zero
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
    
        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0


    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # space O(m + n)
        # time O(m.n)

        m = len(matrix)
        n = len(matrix[0])

        zero_r = set()
        zero_c = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_r.add(i)
                    zero_c.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in zero_r or j in zero_c:
                    matrix[i][j] = 0
        
        

# %% [markdown]
# ## 36. Valid Sudoku
# 
# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = ord(board[i][j]) - ord("1")
                    box_id = (i // 3) * 3 + (j // 3)
                    if rows[i][num] or cols[j][num] or boxes[box_id][num]:
                        return False
                    rows[i][num] = cols[j][num] = boxes[box_id][num] = True
        
        return True


    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        # verify rows
        for i in range(9):
            n_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in n_set:
                    return False
                n_set.add(board[i][j])

        
        # verify cols
        for j in range(9):
            n_set = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in n_set:
                    return False
                n_set.add(board[i][j])
        
        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):    
                sub_box = [x[j: j+ 3] for x in board[i:i + 3]]
                # print(sub_box)
                n_set = set()
                for m in range(3):
                    for n in range(3):
                        if sub_box[m][n] != "." and sub_box[m][n] in n_set:
                            return False
                        n_set.add(sub_box[m][n])

        return True        





        

# %% [markdown]
# ## 54. Spiral Matrix
# 
# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        top, down = 0, m - 1
        # n_ele = m * n
        # while n_ele > 0:

        while left <= right and top <= down:
            # left -> right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
                # n_ele -= 1
            top += 1

            # up -> down
            for r in range(top, down + 1):
                # print(r, right)
                res.append(matrix[r][right])
                # n_ele -= 1
            right -= 1

            # right -> left
            if top <= down:
                for c in range(right, left -1, -1):
                    res.append(matrix[down][c])
                    # n_ele -= 1
                down -= 1

            if left <= right:
                # down -> up
                for r in range(down, top - 1, -1):
                    res.append(matrix[r][left])
                    # n_ele -= 1
                left += 1

        return res


# %% [markdown]
# ## 289. Game of Life
# 
# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150

# %%
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m  = len(board)
        n = len(board[0])
        rep_map = {0: 0, 1: 1, 2: 0, 3: 1}  # live -> dead, dead -> live

        def next_state(x, y):
            n_ones = 0
            n_zeros = 0
            for (i, j) in [(x-1,y-1), (x-1,y), (x-1, y+1),(x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]:
                if 0 <= i < m and 0 <= j < n:
                    if board[i][j] == 0 or board[i][j] == 3: # dead + dead but going to be live
                        n_zeros += 1
                    if board[i][j] == 1 or board[i][j] == 2:  # live + live but going to die
                        n_ones += 1

            curr_state = board[x][y]
            if curr_state == 1:
                if n_ones < 2:  # under-population
                    next_state = 2
                elif n_ones == 2 or n_ones == 3:  # live
                    next_state = 1
                else: # over population
                    next_state = 2
            # else:
            elif curr_state == 0:
                if n_ones == 3: # reproduction
                    next_state = 3
                else:
                    next_state = 0
            else: # this will never reach
                next_state = curr_state

            return next_state


        for i in range(m):
            for j in range(n):
                board[i][j] = next_state(i, j)
        

        for i in range(m):
            for j in range(n):
                board[i][j] = rep_map[board[i][j]]

# %% [markdown]
# ## 5. Longest Palindromic Substring
# 
# https://leetcode.com/problems/longest-palindromic-substring/description/

# %%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            """expand from center to outward"""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1 
            return s[l + 1: r]
        n = len(s)
        
        if n == 1:
            return s
        res = ""

        for i in range(n):
            # for r in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        
        return res


