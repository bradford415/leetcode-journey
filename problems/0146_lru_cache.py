from typing import List, Optional

class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self._cap = capacity

        # dummy values; left = LRU, right = Most Recent
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # initially, set them equal to each other
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        # """Insert to the right (in between rights previous and right)"""
        node.next = self.right
        node.prev = self.right.prev
        node.prev.next = node
        self.right.prev = node
        

    def remove(self, node):
        """Remove node from doubly linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # remove node from tlist then re-insert it so it's to the most right of the list (most recently used)
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key=key, value=value)
        self.insert(self.cache[key])

        if len(self.cache) > self._cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



if __name__ == "__main__":

    # input = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    
    solution = LRUCache()

    ret = solution.functionName(case_1)
    print(ret)
