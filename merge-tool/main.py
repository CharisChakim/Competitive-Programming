def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i+k]
        merged = ''
        for char in substring:
            if char not in merged:
                merged += char
        print(merged)