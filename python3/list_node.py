# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list_to_list_node(cls, numbers: list[int]):
        dummy_root = ListNode(0)
        ptr = dummy_root
        for number in numbers:
            ptr.next = ListNode(int(number))
            ptr = ptr.next

        ptr = dummy_root.next
        return ptr

    @classmethod
    def list_node_to_list(cls, numbers) -> list[int]:
        res = []
        head = numbers
        while head != None:
            res.append(head.val)
            head = head.next
        return res

    def __eq__(self, other) -> bool:
        if other != None:
            if self.val == other.val:
                if self.next == other.next == None:
                    return True
                else:
                    return self.next == other.next
        return False

    def __str__(self) -> str:
        return str(self.val)
