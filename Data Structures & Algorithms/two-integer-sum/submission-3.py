class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer={}
        #n=len(nums)
        for i,val in enumerate(nums):
            diff=target-nums[i]
            if diff in answer:
                return [answer[diff],i]
            answer[val]=i
        