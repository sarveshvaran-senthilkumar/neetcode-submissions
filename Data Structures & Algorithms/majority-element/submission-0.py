class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer={}
        for i,val in enumerate(nums):
            if val not in answer:
                answer[val]=1
            else:
                answer[val]+=1
        for val in answer:
            if answer[val] > len(nums)// 2:
                return val