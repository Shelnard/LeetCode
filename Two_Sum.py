#给定义一个整数数组和一个目标值，找出数组中和为目标值的两个数
def two_sum(nums, target_num):
    result = []
    nums_len = len(nums)
    for i in range(nums_len - 1):
        for j in range(i + 1, nums_len):
            sums = nums[i] + nums[j]
            if sums == target_num:
                result.append((i, j))
    return result
