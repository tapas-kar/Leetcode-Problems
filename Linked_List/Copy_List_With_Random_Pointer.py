# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

# Approach 1: Neetcode approach
# Going to do 2 passes - 1st pass will be to make the copy of the actual nodes
# 2nd pass is going to connect all the next and random pointers
# Hash map to store the mappings of the new copy from the old nodes

def copyRandom(head: 'Optional[Node]') -> 'Optional[Node]':
    # we initialize None to None because of the edge case when the next or the random pointer might point to None, in which case None to point to None
    oldToCopy = {None: None}

    # 1st pass - cloning the linked lists nodes and storing it in the hashmap
    curr = head
    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next

    # 2nd pass - where we set the pointers for all the Copy nodes
    curr = head
    while curr:
        # Let's say we are at the first node where curr is at the head of the LL
        # Remember we already created the copy of the current node in the 1st pass above
        # So we get the copy from the hashmap like shown below to set its pointers
        copy = oldToCopy[curr]

        # Then we have to set the next and the random pointers for this copy node otherwise what is the point of getting this node?
        # copy.next
        # copy.random

        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next

    # return the head of the copy list - how do we get the head?
    # our hash map becomes useful one more time - we can take the head of the original linked list and map it to the copy, right?
    return oldToCopy[head]
        
