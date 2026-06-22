# Original solution with inefficient memory complexity
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group = []
        curr = head
        result = None
        last_node = None

        while curr:
            group.append(curr)
            if len(group) == k:
                next_node = curr.next
                for i in range(k-1):
                    node = group[-1 - i]
                    node.next = group[-2 - i]
                
                group[0].next = next_node
                if last_node:
                    last_node.next = curr
                if not result:
                    result = curr
                last_node = group[0]
                curr = last_node
                group = []

            curr = curr.next
        
        return result
# Optimal Solution for memory
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev_tail = dummy

        while True:
            group_tail = prev_tail
            for _ in range(k):
                group_tail = group_tail.next
                if not group_tail:
                    return dummy.next

            prev, curr = None, prev_tail.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            group_head = prev_tail.next
            prev_tail.next = group_tail
            group_head.next = curr
            prev_tail = group_head
        
        return dummy.next
