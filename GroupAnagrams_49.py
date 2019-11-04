## Group Anagrams


class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        res = []
        for s in strs:
            # # 在Python中如果访问字典中不存在的键，会引发KeyError异常。
            # # 因此，可以采用collections.defaultdict来初始化字典。
            # ans = collections.defaultdict(list)


            # 将字符串s先转为列表，按字母顺序a-z排序，再转为字符串
            tmp = "".join(sorted(list(s)))
            # 排好序的字符串如果在字典中就把原来的字符串添加进去
            if tmp in dict:
                dict[tmp] = dict[tmp] + [s]
            else:  # 如果不在字典中，就把排好序的值作为key，原来的字符串[s]作为值添加到字典中
                dict[tmp] = [s]
        for value in dict.values():
            res.append(value)
        return res




a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
