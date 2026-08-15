class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ele=nums[i]
            ans.insert(i,ele)
            ans.insert(i+n,ele)
        return ans
        