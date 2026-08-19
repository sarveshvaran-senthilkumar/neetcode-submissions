class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer={}
        for i in nums:
            if i not in answer:
                answer[i]=1
            else:
                answer[i]+=1
        
        max_count=-1
        ans=-1

        for key,val in answer.items():
            if val>max_count:
                max_count=val
                ans=key
        return ans