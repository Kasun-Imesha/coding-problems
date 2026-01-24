def longest_sub_string(input_string):
    all_substrings = set()
    substring = ""

    for i in range(len(input_string)):
        inter_substring = input_string[i:]

        for x in inter_substring:

            if x not in substring:
                substring = f"{substring}{x}"
            else:
                all_substrings.add(substring)
                substring = ""

    all_substrings = sorted(all_substrings, key=lambda x: len(x), reverse=True)

    return len(all_substrings[0]), all_substrings[0]

for ip in ["abcd", "abacdb", "cvgcgdcwszs"]:
    print(f"{ip} --> {longest_sub_string(ip)}")