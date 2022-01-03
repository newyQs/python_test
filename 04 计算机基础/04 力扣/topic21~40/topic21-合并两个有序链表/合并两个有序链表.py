class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：递归
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


# 方法二：迭代
def merge_two_lists2(l1: ListNode, l2: ListNode) -> ListNode:
    pre_head = ListNode(-1)

    prev = pre_head
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 if l1 is not None else l2

    return pre_head.next
