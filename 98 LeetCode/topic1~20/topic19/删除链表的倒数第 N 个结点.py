class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：计算链表长度
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    def get_length(head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    dummy = ListNode(0, head)
    length = get_length(head)
    cur = dummy
    for i in range(1, length - n + 1):
        cur = cur.next
    cur.next = cur.next.next
    return dummy.next


# 方法二：栈
def remove_nth_from_end2(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    stack = list()
    cur = dummy
    while cur:
        stack.append(cur)
        cur = cur.next

    for i in range(n):
        stack.pop()

    prev = stack[-1]
    prev.next = prev.next.next
    return dummy.next


# 方法三：双指针
def remove_nth_from_end3(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = head
    second = dummy
    for i in range(n):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next
