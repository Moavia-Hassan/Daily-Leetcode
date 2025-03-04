class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr) -1
        left = 0
        right = size

        if size+1 < 3:
            return False

        while left+1 < size and arr[left] < arr[left+1]:
            left += 1
        while right-1 >= 0 and arr[right] < arr[right - 1]:
            right -= 1
        return left == right and left > 0 and right < size