# length of substring with non repeated characters
    # 'abcabcbb' -> 3
    # 'bbbbb' -> 1
    # 'pwwkew' -> 3
    # 'dvdf' -> 3
    # 'au' -> 2
    # 'tmmzuxt' -> 5
def lengthOfLongestSubstring(s):
        tem=''
        l=0
        for j in range(len(s)):
            while  j<len(s) and s[j] not in tem:
                tem+=s[j]
                j+=1
            if l<len(tem):
                l=len(tem)
        return l

string=input('enter a string: ')
print(lengthOfLongestSubstring(string))