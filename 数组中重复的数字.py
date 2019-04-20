#在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
#请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

#方法一
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numbers.sort()
        flag=False
        for i in range(len(numbers)-1):
            if numbers[i]==numbers[i+1]:
                flag=True
                duplication[0]=numbers[i]
                break
        return flag

    
#方法二
# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        c=collections.Counter(numbers)
        for v,k in c.items():
            if k>1:
                duplication[0]=v
                return True
        return False

    
#方法三
#我最直接的想法就是构造一个容量为N的辅助数组B，原数组A中每个数对应B中下标，首次命中，B中对应元素+1。
#如果某次命中时，B中对应的不为0，说明，前边已经有一样数字了，那它就是重复的了。
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        l=[0]*len(numbers)
        for i in range(len(numbers)):
            a=numbers[i]
            l[a]=l[a]+1
        for i in range(len(l)):
            if l[i]>1:
                duplication[0]=i
                return True
        return False
