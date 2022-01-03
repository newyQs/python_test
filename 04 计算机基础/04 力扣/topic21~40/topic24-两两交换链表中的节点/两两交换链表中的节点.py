# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：递归
def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    return new_head


# 方法二：迭代
def swap_pairs2(head: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    dummy_head.next = head
    temp = dummy_head
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return dummy_head.next
