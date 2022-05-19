class MyHashSet:

    def __init__(self):
        self.keyrange=10000
        self.bucket = [[] for i in range(self.keyrange)]
        

    def add(self, key: int) -> None:
        bucketindex = key%self.keyrange
        curr = self.bucket[bucketindex]
        if not curr:
            self.bucket[bucketindex] = ListNode(key,None)
            return
        while curr != None:
            if curr.value == key:
                return
            if curr.next:
                curr = curr.next
            else:
                curr.next = ListNode(key,None)
            
    def remove(self, key: int) -> None:
        bucketindex = key%self.keyrange
        curr = self.bucket[bucketindex]
        if not curr:
            return
        if curr.value == key:
            self.bucket[bucketindex] = curr.next
        while curr.next:
            if curr.next.value == key:
                curr.next = curr.next.next
                return
            curr=curr.next
        

    def contains(self, key: int) -> bool:
        bucketindex = key%self.keyrange
        curr = self.bucket[bucketindex]
        if not curr:
            return False
        while curr is not None:
            if curr.value == key:
                return True
            curr = curr.next
        return False
class ListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)