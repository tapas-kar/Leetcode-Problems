# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# Approach 1 - Neetcode

# We need to define this class of Node because each of the key-value we put, get, or change the order of to maintain the order of least recently used key-value pair, 
# we are going to use a Node to store that that will inherently have a key-value pair attribute but also have previous and next pointers to point to 
# either the left Node - which will keep track of the least recently used cache value OR the right node - which will keep track of the most recently used cache value
# initially these previous and next pointers will point to None because these have not been hooked up to any other thing yet
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # this is the inherent attribute that the problem gives us, which covers this part of the problem
        # Initialize the LRU cache with positive size capacity
        self.cap = capacity

        # this is the hashmap that we define that will hold the key-value pairings of which key maps to which nodes
        self.cache = {}

        # for the overall cache object mechanism, we define the fact that there will be a left node and a right node - which will help us keep track of the least recently used cache value
        # Left Node => Least Recently Used cache value.......Most Recently Used cache value <= Right Node
        # Initially, we are going to initialize these Nodes with a default value of key - 0 and value - 0
        # And initially, these Left and Right nodes will be hooked up to each other as if there is nothing in the middle when this LRU object is instantiated
        # This is where we see our Node class get used for the first time
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        # to remove a Node from its current position, we need to take the pointer from its previous Node and set its next pointer to the next of the current node and take the previous pointer of the next node and set it to the previous of the current node
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node:Node) -> None:
        # to insert a node into the cache, we need to set the next of the current node to the right node and set the prev of the current node to the left node
        prev = self.right.prev
        nxt = self.right
        # inserting the node in between now
        prev.next = nxt.prev = node
        node.next = nxt # which is self.right, the next of the current node will point to the right most node
        node.prev = prev # which is self.right.prev, the prev of the current node will point to the node the node that was being pointed by the self.right.prev earlier

    
    def get(self, key: int) -> int:
        # According to the question, Return the value of the key if the key exists, otherwise return -1
        # What this part of the function also wants us to do, which is not explicitly stated in the problem is that:
        # when a key-value pair is fetched or "got" from the cache, it also wants us to move the order of this key-value pair to the Right Most side of the whole cache because this is technically the Most Recent Used key-value pair that was accessed
        # That means removing this key-value Node from its current position and moving it to the right most position
        if key in self.cache:
            # before we return the value of the key that was queried with this get method, we want to remove this Node from its current psotion and move it all the way to the right position
            # for that we can use a couple of helper methods that let us do that - remove and insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # After the above re-ordering of the Node, since this key-value pairing is a Node, we want to return the value of that Node when it is fetched
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:


        # My attempt below:
        # # For this part of the question, Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        # # 1st part - Update the value of the key if the key exists
        # # 2nd part - Otherwise, add the key-value pair to the cache

        # # So 1st part - if the key exists in the cache, update the value of the key
        # if key in self.cache:
        #     self.cache[key] = value
        #     # Again, that also means, which is not explicitly stated in the problem, that since this key-value pair just got updated in the cache,
        #     # we need to remove it from its current position and move it all the way to the right position, since this is now the most recently used Node in the cache
        #     self.remove(self.cache[key])
        #     self.insert(self.cache[key])
        
        # # Now 2nd part - If the key DOES NOT EXIST in the cache, then we need to make a new Node with that key-value pair
        # # Technically, this should be inserted to the right most position since it is the Most Recent Node that was created
        # self.cache[key] = Node(key, value)
        # self.insert(self.cache[key])

        # # Now 3rd part - If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        # if len(self.cache) > self.cap:
        #     # 2 things here:
        #     # 1. remove the Node from the Left hand side of the cache, since that is the least recently used Node
        #     # 2. delete that key-value pairing from the cache, since it has exceeded its capacity
        #     self.remove(self.cache[self.left.next])
        #     del self.cache[self.left.next]





        # After looking at Neetcode's approach:
        # If the key is already in the cache then, we need to update that key-value pairing in the cache
        # To do that, we:
        #       first remove the current key-value Node with the existing key
        #       create a new Node with the key and the value argument that is passed into the put method
        #       insert that Node in the cache
        #       By the way, by default, when we say we are inserting some Node with the helper function, we mean we are inserting it into the right most position
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # lastly, when we encounter a case where the cache has reached its capacity
        # we check if the length of the cache is greater than the capacity (attribute initialized as part of the LRU object) AFTER the new key-value Node has been inserted
        # we can check the length by doing len(self.cache) because cache has been initialized as a dictionary attribute of the LRU object
        if len(self.cache) > self.cap:
            # if the length of the cache in the current state AFTER inserting the new key-value Node is greater than the original cache capacity then.
            # we set the lru node to be the node, which is to the next of the self.left node
            lru = self.left.next

            # we use the helper function to remove that node
            self.remove(lru)

            # AND we also delete the key of that lru node and we can access it by doing lru.key because lru is technically a Node and we have a key attribute for a Node defined in the beginning
            del self.cache[lru.key]
