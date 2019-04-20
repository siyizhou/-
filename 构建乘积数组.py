#给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        f=[1]*len(A)
        b=[1]*len(A)
        B=[1]*len(A)
        for i in range(1,len(A)):
            f[i]=f[i-1]*A[i-1]
        for i in range(len(A)-2,-1,-1):
            b[i]=b[i+1]*A[i+1]
        for i in range(len(A)):
            B[i]=f[i]*b[i]
        return B
