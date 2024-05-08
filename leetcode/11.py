class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left]>=height[right]: 
                right-=1
            else: 
                left+=1
        return max_area
    
# O(n)
    