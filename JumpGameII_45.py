## 跳跃游戏：
# 给定一串数字，数字的值表示在这个位置可以直接到达的最大长度，
# 我们要求的则是到达最后一个数字所需要的最小步数


class Solution:
    def jump(self, nums):
        step = 0  # 当前步数
        last = 0  # 上一跳可达的最远距离
        cur = 0  # 当前一跳可达的最远距离

        for i in range(len(nums)):
            # 如果下标i超过上一跳可达的最远距离，步数+1；
            # 如果i<=last，代表这个位置可以由上一跳最大位置直接到达
            if i > last:
                last = cur  # 并且重新定义上一跳可达最远距离
                step += 1
            # 每次都需要更新当前位置可以到达的最大距离
            cur = max(cur, i+nums[i])
        # 越过最后一个位置也算到达
        if cur >= len(nums)-1:
            return step
        else:
            return 0


a = Solution()
print(a.jump([3, 2, 1, 0, 4]))
