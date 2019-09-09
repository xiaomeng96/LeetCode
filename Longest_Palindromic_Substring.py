# 最长回文子串：正读和反读都是相同的字符串
# 用到manacher算法
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s) <= 1:
        #     return s
        # s = '#' + '#'.join(s) + '#'
        # RL = [0]*len(s)  # 复制
        # MaxRight = 0
        # pos = 0
        # MaxLen = 0
        #
        # for i in range(len(s)):
        #     if i < MaxRight:
        #         # i的两种情况
        #         # https://segmentfault.com/a/1190000003914228
        #         RL[i] = min(RL[2*pos - i], MaxRight - i)
        #     else:
        #         RL[i] = 1
        #     # 尝试扩展，注意处理边界
        #     while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
        #         RL[i] += 1
        #     # 更新MaxRight,pos
        #     if RL[i]+i-1 > MaxRight:
        #         MaxRight = RL[i] + i - 1
        #         pos = i
        #     # 更新最长回文子串的长度
        #     MaxLen = max(MaxLen, RL[i]-1)
        # Maxstr = s[pos - int(RL[pos]/2):pos+int(RL[pos]/2)+1]
        # # print(pos, s[pos])
        # # print(Maxstr)
        # Maxstr = Maxstr.split('#')
        # Maxstr = "".join(Maxstr)
        # # print(Maxstr)
        # return Maxstr


        s_list = [str for str in s]
        string = '#' + '#'.join(s_list) + '#'
        max_length = 0  # 最大长度
        pos = 0  # 最大子串的中心位置
        length = len(string)
        for index in range(0, length):
            s_length = 0
            # 找以该位置为中心的最大子串
            for i in range(1, index+1):
                if index + i < len(string) and string[index-i] == string[index+i]:
                    s_length += 1
                else:
                    break
            if max_length < s_length:
                max_length = s_length
                pos = index
        # print(pos, string[pos])
        max_str = string[pos - max_length: pos + max_length]
        max_str = max_str.split('#')
        max_str = "".join(max_str)
        # print(max_str)
        return max_str

if __name__ == '__main__':
    s = "babad"
    s2 = "cbbd"
    s3 = 'ac'
    sl = Solution()
    print(sl.longestPalindrome(s3))




