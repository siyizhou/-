class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a=ListNode(3)
a.val #3

a.val=4
a.val #4

a.next=ListNode(4)
b=a.next 
b.val #4

b.next is None #True
b.next==None #True

if b:
    print(3)
# 3
