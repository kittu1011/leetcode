# Original Solution without dummy nodes
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.arr = [None for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        curr = self.arr[self.hash(key)]
        if not curr:
            self.arr[self.hash(key)] = ListNode(key,value)
            return
        prev = None
        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key,value)
            

    def get(self, key: int) -> int:
        curr = self.arr[self.hash(key)]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.arr[self.hash(key)]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                   prev.next = curr.next 
                else:
                    self.arr[self.hash(key)] = curr.next # this is like pop front
                return
            prev = curr
            curr = curr.next

    def hash(self, key: int) -> int:
        return key % len(self.arr)
# Optimal O(1) Time solution
class MyHashMap:
    def __init__(self):
        self.arr = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        curr = self.arr[key] = value
        
    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1
    