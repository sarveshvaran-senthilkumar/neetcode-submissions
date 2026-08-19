class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        
        arr=[]

        for idx, val in count.items():
            arr.append([val,idx])
        arr.sort(reverse=True)

        ans=[]
        for i in range(k):
            ans.append(arr[i][1])

        return ans