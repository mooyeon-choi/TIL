from collections import deque

# Node 구현
class Node(object):
    """
    A single node of a trie.
    
    Children of nodes are defined in a dictionary
    where each (key, value) pair is in the form of
    (Node.key, Node() object).
    """
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

# Trie 구현
class Trie(object):
    def __init__(self):
        self.head = Node(None)

    
    """
    Trie에 문자열 삽입
    """
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # string의 마지막 글자 차례면
        # node의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string
    

    """
    주어진 단어 string이 트라이에 존재하는지 여부를 반환
    """
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        # string의 마지막 글자에 다달았을때,
        # curr_node에 data가 있다면 string이 트라이에 존재 하는 것.
        if (curr_node.data != None):
            return True

    
    """
    주어진 prefix로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환
    """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # 트라이에서 prefix 를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # bfs 로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        que = deque()
        que += list(subtrie.children.values())
        
        while que:
            curr = que.popleft()
            if curr.data != None:
                result.append(curr.data)

            que += list(curr.children.values())

        return result


# Test
t = Trie()
words = ["romane", "romanus", "romulus", "ruben", "rubens", "ruber", "rubicon", "ruler"]
for word in words:
    t.insert(word)

print(t.search("romulus"))
print(t.search("ruler"))
print(t.search("rulere"))
print(t.search("romunus"))
print(t.starts_with("ro"))
print(t.starts_with("rube"))