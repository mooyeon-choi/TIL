class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:
            return

        cur = self.head
        print('[', end=' ')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertAt(self, idx, node):  # idx: 삽입 위치, node: 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:
                node.next = cur
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
            else:
                node.next = cur
                prev.next = node
            self.size += 1


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    mylist = List()
    for _ in range(m):
        list(map(int, input().split()))

    prev_list.reverse()
    print('#{}'.format(tc), *prev_list[:10])
