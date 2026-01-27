s = "abcde"
ws = ["b", "bb", "abd", "ace", "abcde", "aeb", ""]


# O(n*m) time complexity
def is_substring(s: str, w: str) -> bool:
    tmp_s = s
    
    if not w:
        return False
        
    for i in range(len(w)):
        cw = w[i]
        for j in range(len(tmp_s)):
            cs = tmp_s[j]
            
            if cw == cs:
                tmp_s = tmp_s[j+1:]
                break
        else:
            return False
    return True


def count_substrings(s: str, ws: list) -> int:
    return sum(1 for w in ws if is_substring(s, w))


# O(n + m) time complexity
def is_substring_efficient(s: str, w: str) -> bool:
    l_s = len(s)
    l_w = len(w)
    
    if l_w == 0:
        return False

    s_idx, w_idx = 0, 0
    
    while s_idx < l_s and w_idx < l_w:
        if s[s_idx] == w[w_idx]:
            w_idx += 1
        s_idx += 1
        
    return w_idx == l_w


def count_substrings_efficient(s: str, ws: list) -> int:
    return sum(1 for w in ws if is_substring_efficient(s, w))

    
if __name__ == "__main__":
    for w in ws:
        print(f"{w} --> {is_substring(s, w)} -- {is_substring_efficient(s, w)}")
        
    print(count_substrings(s, ws))    
    print(count_substrings_efficient(s, ws))
            