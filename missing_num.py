class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and nums[0]==1:
            return 0
        
        if len(nums) == 1 and nums[0]==0:
            return 1
            

        
        nums.sort()
        if nums[0] != 0:
            return 0
        max_num = nums[-1]
        
        sum_array = sum(nums)
        real_sum = (max_num*(max_num+1))//2
        print("real sum", real_sum)
        missing_num = real_sum - sum_array
        print("missing num", missing_num)
        if real_sum == sum_array:
            return max_num+1
        return missing_num
