## 装水最多的容器

# 最大桶底，利用首尾两个双指针low，high；
# height[low] < height[high]时，low向右移；
# height[low] >= height[high]时，high向左移
# 桶底保持最大，保证每次选取的线最长
def maxArea(height):

    n =len(height)
    max_area = 0
    low = 0
    high = n - 1
    while low < high:
        if height[low] < height[high]:
            area = (high-low) * height[low]
            low += 1
        else:
            area = (high-low) * height[high]
            high -= 1
        if max_area < area:
            max_area = area
    return max_area



print(maxArea([1,8,6,2,5,4,8,3,7]))