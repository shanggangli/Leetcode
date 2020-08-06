#-*- codeing=utf-8 -*-
#@time: 2020/8/6 22:03
#@Author: Shang-gang Lee
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = []
        nums = 1  # 长度要1开始，因为只要出现字母，长度至少为1
        n = 1
        for i in s:
            if n == 1:  # 开始的第一个值必须插入列表中
                res.append(i)
                n = 2
            else:
                if i not in res:  # 如何在列表中没有该值，则插入列表
                    res.append(i)
                    j = len(res)  # 计算当前列表大小
                    nums = max(nums, j)  # 和历史记录比，取最大的列表长度
                else:
                    index = res.index(i)  # 列表中以存在该值，则获取其索引并将其前面的值都删去
                    del res[:index + 1]  # 需要注意，删除区间是左闭右开的
                    res.append(i)  # 然后再把当前值插入其中

        return nums  # 最后返回最大的列表长度

t=Solution()
print(t.lengthOfLongestSubstring('bsadagabb')) #4