#-*- codeing=utf-8 -*-
#@time: 2020/8/14 20:48
#@Author: Shang-gang Lee
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack
t=Solution()
print(t.isValid("(]){}[]"))

