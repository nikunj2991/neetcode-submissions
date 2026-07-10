# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        self.head = head
        """
            [a] - > [b] -> [c] -> [d]

            prev = [a]
            curr = [b]
            
            reverse_association(a, b)
                    
        """
        self.__reverse(self.head, self.head.next)
        return self.head

    def __reverse(self, prev: ListNode, curr: ListNode) -> ListNode:
        self.head = curr
        while curr.next:
            self.__reverse(curr, curr.next)
        
        curr.next = prev
        prev.next = None

        