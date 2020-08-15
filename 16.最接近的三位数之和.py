#-*- codeing=utf-8 -*-
#@time: 2020/8/15 11:18
#@Author: Shang-gang Lee

class Solution:
    def threeSumClosest(self, nums,target):
        n=len(nums)
        if (not nums or n<3):
            return None
        nums.sort()
        init=nums[0]+nums[1]+nums[2]
        for i in range(n):
            L=i+1
            R=n-1
            while(L<R):
                temp=nums[i]+nums[L]+nums[R]
                if abs(target-temp)<abs(target-init):   #取绝对值最小的那个
                    init=temp
                if (temp>target):   #如果大于target 说明还有减小的空间 所以R-1
                    R=R-1
                elif(temp<target):  #如果小于target 说明还有增大的空间 所以L+1
                    L=L+1
                else: return init   #如果存在等于target的情况，则返回
        return init #否则返回最小的init
t=Solution()
print(t.threeSumClosest([0,2,1,-3],1))