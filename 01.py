#-*- codeing=utf-8 -*-
#@time: 2020/8/6 22:31
#@Author: Shang-gang Lee

class Solution:
    def twoSum(self, nums:list, target: int):
        hashmap={}
        for index,num in enumerate(nums):   #用字典做哈希表
            hashmap[num]=index
        for i ,num in enumerate(nums):
            j=hashmap.get(target-num)       #在哈希表中寻找满足 target-num 的值
            if j is not None and i!=j:      #如果该值存在并且不等于i，则返回
                return [i,j]
t=Solution()
print(t.twoSum([2, 7, 11, 15],9)) #[0,1]