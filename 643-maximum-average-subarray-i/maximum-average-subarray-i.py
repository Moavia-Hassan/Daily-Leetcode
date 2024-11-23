class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        # def get_average(arr,k):
        #     sum = 0
        #     for i in arr:
        #         sum += i
        #     return sum/k
        # max = 0
        # for i in range(len(nums) - k + 1):
        #     arr = nums[i:i+k]
        #     average = get_average(arr,k)
        #     if  average > max:
        #         max = average
        # return max
        n = len(nums)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, n):
            curr_sum += nums[i] - nums[i-k]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum / k