class Solution:
    def maxArea(self, heights: List[int]) -> int:
        M = 0
        l,r = 0, len(heights) - 1
        while l < r:
            M = max(M, (r-l) * min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return M