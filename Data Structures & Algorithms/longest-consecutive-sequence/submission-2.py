class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(nums)
        n=len(s)
        longest=1
        curr=1
        if n==0:
            return 0
        for i in range(1,n):
            if s[i]==s[i-1]:
                continue
            elif s[i]==s[i-1]+1:
                curr+=1
            else:
                longest=max(longest,curr)
                curr=1
        longest=max(longest,curr)
        return longest

