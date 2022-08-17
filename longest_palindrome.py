"""Number 5: Longest Palindrome"""


def longest_palindrome(s: str) -> str:
    longest = s[0]
    for i in range(1, len(s)):
        j = 1
        palindrome = s[i]
        while i - j >= 0 and i + j < len(s):
            if s[i-j] != s[i+j]:
                break
            else:
                palindrome = s[i-j] + palindrome + s[i+j]
                longest = palindrome if len(palindrome) > len(longest) else longest
            j += 1

        palindrome = ''
        if s[i-1] == s[i]:
            l = i-1
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    palindrome = s[l] + palindrome + s[r]
                    longest = palindrome if len(palindrome) > len(longest) else longest
                else:
                    break
                l -= 1
                r += 1

    return longest


print(longest_palindrome('abbbba'))
