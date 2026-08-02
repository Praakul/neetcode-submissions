class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            ele1 = numbers[left] 
            ele2 = numbers[right] 

            if ele1 + ele2 == target:
                return [left+1, right+1]
            elif ele1 + ele2 < target:
                left += 1
            if ele1 + ele2 > target:
                right -= 1
        return