class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, array):
        for arr in array:
            self.append(arr)

    def add(self, location, data):
        new_node = ListNode(data)
        if location == 0:
            new_node.next = self.head
            self.head = new_node
        elif location > 0:
            pre = self.head
            for i in range(location-1):
                pre = pre.next
            new_node.next = pre.next
            pre.next = new_node

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = ListNode(data)
        # if not self.head:
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, location):
        if location == 0:
            self.head = self.head.next
        elif location > 0:
            pre = self.head
            for i in range(location-1):
                pre = pre.next
            pre.next = pre.next.next

    def update(self, location, data):
        current = self.head
        for i in range(location):
            current = current.next
        current.data = data

    def get(self, location):
        current = self.head
        for i in range(location):
            current = current.next
        print(current.data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        pre = None
        cur = self.head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


def __main__(self):
    ll.create([1, 2, 3, 4, 5])
    ll.add(1, 2)
    ll.append(8)
    ll.delete(0)
    ll.update(3, 5)
    ll.display()
    ll.head = ll.reverse()
    ll.display()
    # ll.get(4)


ll = LinkedList()
__main__(ll)
