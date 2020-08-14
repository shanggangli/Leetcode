#-*- codeing=utf-8 -*-
#@time: 2020/8/11 21:48
#@Author: Shang-gang Lee

#方法1： 暴力法   时间复杂度 : O((n + m)log(n + m))           空间复杂度 : O(1)
class Solution:
    def merge(self, nums1, m, nums2,n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted(nums1[:m]+nums2)

#方法2用双指针,从前先后。 比较两个list，取小的插进num1中. 时间复杂度 : O(n + m)    空间复杂度 : O(m)
class Solution1:
    def merge(self, nums1, m, nums2,n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy=nums1[:m]
        nums1[:]=[]
        p1,p2=0,0
        while p1<m and p2<n:
            if nums1_copy[p1]<nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1+=1
            else:
                nums1.append(nums2[p2])
                p2+=1
                # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

#方法3:双指针，从后先前.  时间复杂度:O(n + m)      空间复杂度:O(1)
class Solution2:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p=m+n-1     #最末尾的指针
        p1=m-1
        p2=n-1
        while p2>=0 and p1>=0:
            if nums2[p2]>nums1[p1]:     #把最大的插入num1的最后
                nums1[p]=nums2[p2]
                p2-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
            p-=1
        nums1[:p2+1]=nums2[:p2+1]      #如何num2中有漏的数据，则添加到num1中