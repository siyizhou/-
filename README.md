# 栈
栈是一种特殊的线性表，仅能在线性表的一端操作，栈顶允许操作，栈底不允许操作。<br>
栈的特性：后进先出<br>
先出栈顶的元素<br>

https://blog.51cto.com/9291927/2063393<br>
https://blog.csdn.net/xiangxizhishi/article/details/79120227<br>

注：线性表是最基本、最简单、也是最常用的一种数据结构。线性表（linear list）是数据结构的一种，一个线性表是n个具有相同特性的数据元素的有限序列。<br>

# 队列
队列是一种特殊的线性表<br>
特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作<br>
和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。


# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
栈A用来作入队列<br> 
栈B用来出队列，当栈B为空时，栈A全部出栈到栈B,栈B再出栈（即出队列）<br> 

整体思路是:<br>
1.元素先依次进入栈1，再从栈1依次弹出到栈2，然后弹出栈2顶部的元素，整个过程就是一个队列的先进先出
2，但是在交换元素的时候需要判断两个栈的元素情况：“进队列时”，队列中是还还有元素，若有，说明栈2中的元素不为空，此时就先将栈2的元素倒回到栈1 中，保持在“进队列状态”。“出队列时”，将栈1的元素全部弹到栈2中，保持在“出队列状态”。所以要做的判断是，进时，栈2是否为空，不为空，则栈2元素倒回到栈1，出时，将栈1元素全部弹到栈2中，直到栈1为空。
