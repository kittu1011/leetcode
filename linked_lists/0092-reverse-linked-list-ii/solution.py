class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dum = ListNode(next=head)
        dummy = dum
        curr = head
        for _ in range(left - 1):
            curr = curr.next
            dummy = dummy.next
        
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        dummy.next.next = curr
        dummy.next = prev
        return dum.next
        