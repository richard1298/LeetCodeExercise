class MyHashMap:

    def __init__(self):
        self.bucketrange = 1000
        self.bucketArray = [[] for i in range(self.bucketrange)]

    def put(self, key: int, value: int) -> None:
        bucketindex = key%self.bucketrange
        curr = self.bucketArray[bucketindex]
        if not curr:
            self.bucketArray[bucketindex] = ListNode([key, value],None)
            #print('array=',self.bucketArray)
            return
        while curr is not None:
            if curr.value[0]==key:
                curr.value[1]=value
                return
            if curr.next:
                curr = curr.next
            else:
                curr.next = ListNode([key, value],None)
                return
        
    def get(self, key: int) -> int:
        bucketindex = key%self.bucketrange
        curr = self.bucketArray[bucketindex]      
        #print('bucketArray=',self.bucketArray)
        result = -1
        #print(curr)
        while curr:
            if curr.value[0]==key:
                result = curr.value[1]
                break
            else:
                curr = curr.next
        return result   
    
    def remove(self, key: int) -> None:
        bucketindex = key%self.bucketrange
        curr = self.bucketArray[bucketindex]
        if not curr:
            return
        if curr.value[0]==key:
            self.bucketArray[bucketindex] = curr.next
            return
        while curr.next:
            if curr.next.value[0]==key:
                curr.next = curr.next.next
                return
            curr = curr.next

class ListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)