class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:
            return

        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']', end='')
