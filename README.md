
# 堆

https://www.jianshu.com/p/6b526aa481b1<br>

堆就是用数组实现的二叉树，所有它没有使用父指针或者子指针。堆根据“堆属性”来排序，“堆属性”决定了树中节点的位置。<br>

## 堆属性
堆分为两种：最大堆和最小堆，两者的差别在于节点的排序方式。<br>

在最大堆中，父节点的值比每一个子节点的值都要大。<br>
在最小堆中，父节点的值比每一个子节点的值都要小。<br>
这就是所谓的“堆属性”，并且这个属性对堆中的每一个节点都成立。<br>

根据这一属性，那么最大堆总是将其中的最大值存放在树的根节点。<br>
而对于最小堆，根节点中的元素总是树中的最小值。<br>
堆属性非常的有用，因为堆常常被当做优先队列使用，因为可以快速的访问到“最重要”的元素。<br>

## 用堆来表示树
使用层次遍历就好了，把树按数组存储起来<br>
如果 i 是节点的索引(即在数组中的索引)，那么下面的公式就给出了它的父节点和子节点在数组中的位置：<br>

parent(i) = floor((i - 1)/2)<br>
left(i)   = 2i + 1<br>
right(i)  = 2i + 2<br>
注： right(i) 就是简单的 left(i) + 1,要保证是有效索引
