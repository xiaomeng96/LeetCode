## 跳跃游戏：
# https://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html
# 给定一串数字，数字的值表示在这个位置可以直接到达的最大长度，
# 我们要求的则是到达最后一个数字所需要的最小步数
# 题目假设总能到达数组的最后索引

class Solution:
    def jump(self, nums):
        step = 0  # 当前步数
        last = 0  # 上一跳可达的最远距离
        cur = 0  # 当前一跳可达的最远距离

        for i in range(len(nums)):
            # 如果i<=last，代表这个位置可以由上一跳最大位置直接到达
            # 如果下标i超过上一跳可达的最远距离，步数+1；
            if i > last:
                last = cur  # 并且重新定义上一跳可达最远距离
                step += 1
                # 当前的覆盖范围已经到了最后，不需要更新步数了
                if cur >= len(nums) - 1:
                    break
            # 每次都需要更新当前位置可以到达的最大距离
            cur = max(cur, i+nums[i])

        return step


a = Solution()
print(a.jump([3, 2, 1, 0, 4]))
