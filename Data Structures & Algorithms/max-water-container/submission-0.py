class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea= 0
        n=len(heights)
        for i in range(n):
            for j in range(i+1,n):
                area = (j-i) * min(heights[i],heights[j])
            
                maxarea=max(maxarea,area)
        return maxarea
        