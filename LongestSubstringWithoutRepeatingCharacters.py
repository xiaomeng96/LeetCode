# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         maxlength = 0
#         s_list = list(s)
#         for i in range(len(s_list)):
#             tmp = [s_list[i]]
#             for j in range(i+1, len(s_list)):
#                 if s_list[j] in tmp:
#                     break
#                 else:
#                     tmp.append(s_list[j])
#             if len(tmp)>maxlength:
#                 maxlength = len(tmp)
#         return maxlength
# 运行超时

# 不重复最长子串的长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """

        :param s:
        :return: int
        """
        ans, start, end = 0, 0, 0
        # 存储当前子串中各字符的个数
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:   # 表明有重复，向右移动起点
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans

a = Solution()
s = 'abcabcbb'
maxL = a.lengthOfLongestSubstring(s)
print(maxL)
