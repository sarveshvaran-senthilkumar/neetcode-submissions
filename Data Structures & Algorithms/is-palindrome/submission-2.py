class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        ans=[]
        for c in s:
            if c.isalnum():
                ans.append(c.lower())
        ss=''.join(ans)
        return ss==ss[::-1]