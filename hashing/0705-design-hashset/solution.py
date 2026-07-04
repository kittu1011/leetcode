# Original Solution
class MyHashSet:
    def __init__(self):
        self.arr = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        return self.arr[key] == True
# Linked list solution with seprate chaining
class ListNode:
    def __init__(self, key: int):
        self.val = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.arr = [ListNode(-1) for _ in range(10000)] # -1 is a sentinel value and we use dummy node

    def add(self, key: int) -> None:
        idx = key % 10000
        curr = self.arr[idx]
        while curr.next: 
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % 10000
        curr = self.arr[idx]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = key % 10000
        curr = self.arr[idx]
        while curr.next:
            if curr.next.val == key: # if key is last element in linked list then we can never check it's value if we check curr.val
                return True
            curr = curr.next
        return False
