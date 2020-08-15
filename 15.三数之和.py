#-*- codeing=utf-8 -*-
#@time: 2020/8/15 10:37
#@Author: Shang-gang Lee

'''
特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
对数组进行排序。
遍历排序后数组：
若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
'''


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()  # 排序 如果nums[i]>0,说明后面的数字之和没有=0的了
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):  # 去除重复
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):  # 去除重复
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):  # 去除重复
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):  # 说明R太大了，应该-1
                    R = R - 1
                else:  # 说明L太小了，应该+1
                    L = L + 1
        return res

t=Solution()
print(t.threeSum([-1,0,1,2,-1,-4]))