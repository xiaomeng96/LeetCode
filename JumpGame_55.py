# https://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html

class Solution:
    def jump(self, nums):
        last = 0  # 上一跳可达的最远距离
        cur = 0  # 当前一跳可达的最远距离

        for i in range(len(nums)):
            # 如果i<=last，代表这个位置可以由上一跳最大位置直接到达
            # 如果下标i>last，需要向前跳一跳才能覆盖位置i；
            if i > last:
                if last == cur:  # 二者相等，说明i走向last的过程中，
                    # 没有找到可以跳过当前位置的最远距离
                    return False
                last = cur  # 并且重新定义上一跳可达最远距离
                # step += 1
                # 当前的覆盖范围已经到了最后，不需要更新步数了
                if cur >= len(nums) - 1:
                    break
            # 每次都需要更新当前位置可以到达的最大距离
            cur = max(cur, i+nums[i])

        return True


a = Solution()
print(a.jump([2,3,1,1,4]))