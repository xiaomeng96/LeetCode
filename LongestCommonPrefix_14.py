## 最长相同前缀


# # 方法一：对strs进行升序排序（按照长度），用最短的strs[0]和剩下的字符串进行比较
# def longestCommonPrefix(strs):
#
#      if len(strs) == 0:
#           return ""
#      strs.sort(key=len)  ## key指定一个函数
#      for i in range(len(strs[0])):
#           for j in range(1, len(strs)):
#                if strs[0][i] != strs[j][i]:
#                     return strs[0][:i]
#      return strs[0]




## 利用min()和max()函数返回strs中最小最大字符串，再比较最小最大字符串
def longestCommonPrefix(strs):
     if not strs:
          return ""
     min_str = min(strs)
     max_str = max(strs)
     print(min_str, max_str)
     for i in range(len(min_str)):
          if min_str[i] != max_str[i]:
               return min_str[:i]
     return min_str




print(longestCommonPrefix(["flower","arrrrow","flightyy"]))