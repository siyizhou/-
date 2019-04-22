# 树
有关树的知识点以及算法题

<br>
知识点参考https://www.cnblogs.com/llguanli/p/7363657.html <br>

<br>
二叉树是一种非常重要的数据结构，非常多其他数据结构都是基于二叉树的基础演变而来的。对于二叉树，有深度遍历和广度遍历，深度遍历有前序、中序以及后序三种遍历方法，广度遍历即我们寻常所说的层次遍历。由于树的定义本身就是递归定义，因此採用递归的方法去实现树的三种遍历不仅easy理解并且代码非常简洁，而对于广度遍历来说，须要其他数据结构的支撑。比方堆了。所以。对于一段代码来说，可读性有时候要比代码本身的效率要重要的多。

四种基本的遍历思想为：<br>
前序遍历：根结点 ---> 左子树 ---> 右子树<br>
中序遍历：左子树---> 根结点 ---> 右子树<br>
后序遍历：左子树 ---> 右子树 ---> 根结点<br>
层次遍历：仅仅需按层次遍历就可以<br>

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:   #有右子树的，那么下一个结点为右子树最左边的一个点
            left1 = pNode.right
            while left1.left:
                left1 = lef1.left
            return left1
        while pNode.next:  #若此结点没有右子树
            temp = pNode.next
            if temp.left==pNode:    #如果是父节点的左结点，则下一个结点即为父节点
                return temp
            pNode = temp
