#定义链表结构
class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None



def create_list(n):
    head = NodeList(1)
    curr = head
    for i in range(2, n + 1):
        new_node = NodeList(i)
        curr.next = new_node
        curr = new_node
    curr.next = head
    return head

def find_last(head):
    p = head
    while p.next != p:
        # Skip the next node and point to the next next node
        p.next = p.next.next
        p = p.next
    return p.val
#主函数
import sys
for i in sys.stdin:
    n = int(i)
    head = create_list(n)
    print(find_last(head))
