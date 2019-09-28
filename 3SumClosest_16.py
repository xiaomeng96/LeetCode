## 给定数组和目标数，在数组中找到唯一三个数，这三个数的和接近于目标数，并返回这三个数的和



# 对给定数组nums从小到大排序；
# 固定一个值nums[i]，使用两个指针left=i+1,right=n-1；
# 如果sum小于target，left++右移；
# 如果sum大于target，right--左移；
# 保留最小差值的三数之和
def threeSumClosest(nums, target):

    n = len(nums)
    if n == 3:
        return nums[0]+nums[1]+nums[2]
    min_diff = float('inf')
    min_sum = 0
    # 排序
    nums.sort()
    for i in range(n-2):
        left = i+1
        right = n - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            diff = abs(sum - target)
            # 保留最接近目标的三个数之和
            if diff < min_diff:
                min_diff = diff
                min_sum = sum


            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return sum  # 三个数之和与目标相等，直接返回
    return min_sum

print(threeSumClosest([-1, 2, 1, -4], 1))


