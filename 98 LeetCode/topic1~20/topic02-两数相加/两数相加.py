class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    current = dummy = ListNode()  # 首先创建一个虚拟节点，并创建一个current指针，指向这个节点
    carry, value = 0, 0  # 初始化carry和两个链表对应节点相加的值

    # 下面的while循环中之所以有carry，是为了处理两个链表最后节点相加出现进位的情况
    # 当两个节点都走完而且最后的运算并没有进位时，就不会进入这个循环
    while carry or l1 or l2:
        # 让value先等于carry既有利于下面两个if语句中两个对应节点值相加，
        # 也是为了要处理两个链表最后节点相加出现进位的情况
        value = carry
        # 只要其中一个链表没走完，就需要计算value的值
        # 如果其中一个链表走完，那么下面的计算就是加总carry和其中一个节点的值
        # 如果两个链表都没走完，那么下面的计算就是carry+对应的两个节点的值
        if l1:
            l1, value = l1.next, l1.val + value
        if l2:
            l2, value = l2.next, l2.val + value
        # 为了防止value值大于10，出现进位，需要特殊处理
        # 如果value小于10，下面这行的操作对于carry和value的值都没有影响
        carry, value = divmod(value, 10)
        # 利用value的值创建一个链表节点，并让current.next指向它
        current.next = ListNode(value)
        # 移动current指针到下一个节点
        current = current.next
    # 最后只要返回dummy的下一个节点就是我们想要的答案。
    return dummy.next


def add_two_numbers2(l1: ListNode, l2: ListNode) -> ListNode:
    current = dummy = ListNode()
    carry, value = 0, 0
    while carry or l1 or l2:
        value = carry
        if l1:
            l1, value = l1.next, l1.val + value
        if l2:
            l2, value = l2.next, l2.val + value
        carry, value = divmod(value, 10)
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def add_two_numbers3(l1: ListNode, l2: ListNode) -> ListNode:
    count = 0
    ret = ListNode()
    tmp = ret
    while l1 or l2 or count:
        num = 0
        if l1:
            num += l1.val
            l1 = l1.next
        if l2:
            num += l2.val
            l2 = l2.next
        count, num = divmod(num + count, 10)
        tmp.next = ListNode(num)
        tmp = tmp.next
    return ret.next


def add_two_numbers4(l1: ListNode, l2: ListNode) -> ListNode:
    ret = ListNode()
    count = 0
    tmp = ret
    while l1 or l2 or count:
        if l1:
            count += l1.val
            l1 = l1.next
        if l2:
            count += l2.val
            l2 = l2.next
        count, val = divmod(count, 10)
        tmp.next = ListNode(val)
        tmp = tmp.next
    return ret.next


def add_two_numbers5(l1: ListNode, l2: ListNode) -> ListNode:
    # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
    dummy = p = ListNode()
    s = 0  # 初始化进位 s 为 0
    while l1 or l2 or s:
        # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
        s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        p.next = ListNode(s % 10)  # p.next 指向新链表, 用来创建一个新的链表
        p = p.next  # p 向后遍历
        s //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
        l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
        l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
    return dummy.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点


def add_two_numbers6(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(l1.val + l2.val)
    cur = head
    while l1.next or l2.next:
        l1 = l1.next if l1.next else ListNode()
        l2 = l2.next if l2.next else ListNode()
        cur.next = ListNode(l1.val + l2.val + cur.val // 10)
        cur.val = cur.val % 10
        cur = cur.next
    if cur.val >= 10:
        cur.next = ListNode(cur.val // 10)
        cur.val = cur.val % 10
    return head
