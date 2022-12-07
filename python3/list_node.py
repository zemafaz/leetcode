# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def list_to_list_node(numbers: list[int]):
		dummy_root = ListNode(0)
		ptr = dummy_root
		for number in numbers:
			ptr.next = ListNode(int(number))
			ptr = ptr.next

		ptr = dummy_root.next
		return ptr
	
	def __eq__(self, other) -> bool:
		if other != None:
			if self.val == other.val:
				if self.next == other.next == None:
					return True
				else:
					return self.next == other.next
		return False