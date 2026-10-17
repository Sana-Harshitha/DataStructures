def print_subsequence(s):
    def helper(i,curr):
        if i == len(s):
            print(curr)
            return
        helper(i+1,curr+s[i])
        helper(i+1,curr)
    helper(0,"")
