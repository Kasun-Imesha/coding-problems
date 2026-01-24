# find trailing zeros of a string


def factorial(x: int):
    if x <= 1:
        return 1

    return x * factorial(x - 1)


def find_trail_zeros(num: int):
    count = 0

    for x in str(num)[::-1]:
        if x == "0":
            count += 1
        else:
            break

    return count, factorial(count)


# for x in (1234000, 876, 8760, 763700000):
#     print(f"{x}: {find_trail_zeros(x)}")


########################################

# string segment according to a dictionary

def can_segment(word, dictionary, splits=[], skip=0):
    subw = word[:skip]
    L = len(word)
    has_alt = False

    for i in range(skip, len(word)):
        subw = f"{subw}{word[i]}"

        if subw in dictionary:
            
            if (i+1) < L:
                alt_word = f"{subw}{word[i+1]}"
                
                if alt_word in dictionary:
                    alt_splits = splits.copy()

                    if (i+2) < L:
                        has_alt = True
                        return can_segment(word[i-len(subw)+1:], dictionary, alt_splits, len(alt_word)-1)

                    else:
                        alt_splits.append(alt_word)
                        return True, alt_splits
            
            splits.append(subw)
            subw = ""

    if not subw:
        return True, splits

    if not has_alt:
        return False, splits

# dictionary = ["data", "cam", "camp", "campk", "lack", "dataa"]

# for w in ["datacamp", "datafang", "datacamlack", "datacamplack", "wdatacam", "camcampkdataacampkcam"]:
#     print("---"*20)
#     print(f"{w} --> {can_segment(w, dictionary, [], 0)}")

    
##################################################
# remove duplicates from sorted array

def remove_duplicates(d_list):
    last_el = None
    new_idx = 0
    for i in range(len(d_list)):
        cur_el = d_list[i]
        if last_el != cur_el:
            d_list[new_idx] = cur_el
            new_idx += 1
            last_el = cur_el

    return d_list[:new_idx] 

# x = [1, 1, 2, 2, 2, 3, 4, 5]

# print(f"{x} --> {remove_duplicates(x)}")

#####################################################
#Find the maximum single sell profit

def max_profit_trade(price_list):
    buy_val = None
    sell_val = None

    max_p = None

    for t, val in enumerate(price_list):
        if buy_val is None:
            buy_val = val 

        elif sell_val is None:
            sell_val = val
            max_p = (sell_val - buy_val)

        else:
            op1 = (val - buy_val)
            op2 = (val - sell_val)

            if op1 > max_p and op2 > max_p:
                
                if op1 > op2:
                    sell_val = val
                else:
                    buy_val = sell_val
                    sell_val = val

            elif op1 > max_p:
                sell_val = val

            elif op2 > max_p:
                buy_val = sell_val
                sell_val = val

            max_p = sell_val - buy_val

    return buy_val, sell_val

# for x in [[8,4,12,9,20,1], [8,6,5,4,3,2,1]]:
#     print(f"{x} --> {max_profit_trade(x)}")

###########################################
# find missing number

def find_missing(num_list):
    n = len(num_list) + 1

    exp_sum = n * (1 + n) // 2
    cur_sum = sum(num_list)

    return (exp_sum - cur_sum)

# x = [4,5,3,2,8,1,6]

# print(f"{x} --> {find_missing(x)}")

############################################
# find Pythagoren triplets
import numpy as np


def find_triplets(num_list):
    num_list = sorted(num_list)
    sq_num_list = np.square(num_list)
    L = len(sq_num_list)

    for i in range(0, L -2):
        num1 = sq_num_list[i]

        for j in range(i + 1, L - 1):
            num2 = sq_num_list[j]

            for k in range(j + 1, L): # we can search for num1 + num2 in the sq_num_list[j + 1:] instead of this 3rd loop
                num3 = sq_num_list[k]

                if num1 + num2 == num3:
                    return True, (num_list[i], num_list[j], num_list[k])
    
    return False, None

    
# for x in [[3,1,4,6,5], [10,4,6,12,5], []]:
#     print(f"{x} --> {find_triplets(x)}")

###################################################
# How many ways can you make change with coins and a total amount?

def one_way(coins, amount, cur_list=[]):
    # print(f"{coins} -- {amount} -- {cur_list}")

    if amount == 0:
        return True, cur_list

    coins = np.array(coins)
    valid_coins = coins <= amount
    coins = coins[valid_coins]
    L = len(coins)
    result = []

    if L == 0:
        return False,  []
    
    else:

        for i in range(L)[::-1]:
            sub_list = cur_list.copy()
            sub_list.append(coins[i])
            res, comb = one_way(coins[:i+1], amount-coins[i], sub_list)
            
            if res:

                if comb[0] and isinstance(comb[0], list):
                    comb = comb[0]

                result.append(comb)

        return True, result



# denomination = [1,2,5]
# amount = 5

# print(one_way(denomination, amount, []))

####################################################
#  Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

def find_max_j_i(arr):
    best_i = None
    best_j = None

    max_diff = -1

    for i in range(len(arr) -1):

        for j in range(i, len(arr)):
        
            if arr[j] > arr[i]:
        
                if (best_i is None and best_j is None) or (j - i) > max_diff:
                    best_i = i
                    best_j = j

                    max_diff = (j - i)
                    
    return best_i, best_j, max_diff


# for x in [[20,70,40,50,12,38,98], [10, 3, 2, 4, 5, 6, 7, 8, 18, 0], [10,3,2,4,5,11,7,8,1,4], [0,1,2,3,4,5,0,2,3], [5,1,2,3,6,5,0,2,3]]:
#     print(f"{x} --> {find_max_j_i(x)}")

#################################################
# inverse Range Minimum Query (Not done)

def verifyTree(n, ar):
    print(f"Entering {n} -- {ar} -- {len(ar)}")
    if n == 1:
        return True
        
    childs = ar[-n:]
    parnets = ar[-(n + n // 2): -n]

    print(childs)
    print(parnets)
    
    for i in range(len(parnets)):
        print(parnets[i], childs[2*i], childs[2*i + 1])
        if parnets[i] != min(childs[2*i], childs[2*i + 1]):
            return False
    
    return verifyTree(n // 2, ar[:-n])

# x = [1, 1, 3, 1, 2, 3, 4]
# l = len(x)
# n = (l + 1) // 2
# print(verifyTree(n, x))

#################################################
# magic square

def find_magic_number(s):
    sums = [0] * 8
    # print(s)
    # print(sums)
    for i in range(3):
        # print(s[i], "---")
        sums[i] = sum(s[i])
        sums[3] += s[i][0]
        sums[4] += s[i][1]
        sums[5] += s[i][2]
        sums[6] += s[i][i]
        sums[7] += s[i][2 - i]
    
    print(sums)
    
    sum_count = {}
    for each_sum in sums:
        if each_sum not in sum_count:
           sum_count[each_sum] = 1
        else:
            sum_count[each_sum] += 1

    print(sum_count)        
    magic_num = sorted(sum_count.items(), reverse=True, key=lambda x: x[1])[0][0]
    
    return magic_num

# s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# print(find_magic_number(s))

#####################################################
# find prime numbers

def find_primes(upper_limit: int = 5):
    all_primes = []

    for i in range(upper_limit + 1):
        
        if i < 2:
            continue

        for j in range(2, i):
            if i % j == 0:
                break
        
        else:
            all_primes.append(i)

    return all_primes



# print(f"default --> {find_primes()}")

# for x in [0, 1, 2, 5, 7, 10, 50, 100, 111]:
#     print(f"{x} --> {find_primes(x)}")

############################################
# prime generator

def primes_generator(upper_limit: int = 5):

    for i in range(upper_limit + 1):
        
        if i < 2:
            continue

        for j in range(2, i):
            if i % j == 0:
                break
        
        else:
            yield i


def print_generator(p_gen, x="default"):
    print(f"{x} -->", end=" ")

    while True:

        try:
            print(next(p_gen), end=" ")
        except StopIteration:
            print()
            break 

# p_gen = primes_generator()
# print_generator(p_gen)

# for x in [0, 1, 2, 5, 7, 10, 50, 100, 111]:
#     p_gen = primes_generator(x)
#     print_generator(p_gen, x)

############################################
# prime custom iterator

class Prime:
    """
    Iterator for prime numbers 
    """

    def __init__(self, upper_limit: int=5) -> None:
        self.upper_limit = upper_limit 

    def __iter__(self):
        self.i = 0

        return self
        
    def __next__(self):
        while True:
            if self.i > self.upper_limit:
                raise StopIteration

            if self.i < 2:
                self.i += 1
                continue

            for j in range(2, self.i):
                
                if self.i % j == 0:
                    self.i += 1
                    break
            
            else:
                self.i += 1
                return (self.i - 1)

p = Prime()
p_iter = iter(p)
print_generator(p_iter)

for x in [0, 1, 2, 5, 7, 10, 50, 100, 111]:
    p = Prime(x)
    p_iter = iter(p)
    print_generator(p_iter, x)
