from typing import List, Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else: 
                self._insert_recursively(data, node.right)    
        return
    
    def search(self, data):
        return self._search_recursively(data, self.root)
    
    def _search_recursively(self, data, node):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursively(data, node.left)
        else:
            return self._search_recursively(data, node.right)
    
    def dfs(self, data):
        return self._dfs_search(data, self.root)
    
    def _dfs_search(self, data, node):
        if node is None:
            return False
        if node.data == data:
            return True

        if self._dfs_search(data, node.left):
            return True
        if self._dfs_search(data, node.right):
            return True
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        
        return
    
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
        return

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.data)
        return
    

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[Node]:
        if not inorder or not postorder:
            return None
        
        root = Node(postorder.pop()) 
        inorder_index = inorder.index(root.data)
        root.right = buildTree(inorder[inorder_index+1:], postorder)
        root.left = buildTree(inorder[:inorder_index], postorder)

        return root


tree = BinaryTree()
numbers = [5, 3, 8, 1, 7, 9]
for num in numbers:
    tree.insert(num)

for num in numbers:
    print("number", num, tree.search(num))

print("number 6", tree.search(6))

preorder_traversal = tree.preorder_traversal()
print(preorder_traversal)
assert preorder_traversal == [5, 3, 1, 8, 7, 9]

inorder_traversal = tree.inorder_traversal()
print(inorder_traversal)
assert inorder_traversal == [1, 3, 5, 7, 8, 9]

postorder_traversal = tree.postorder_traversal()
print(postorder_traversal)
assert postorder_traversal == [1, 3, 7, 9, 8, 5]


new_tree = buildTree(inorder_traversal, postorder_traversal)
print(new_tree)


for num in numbers:
    print("dfs number", num, tree.dfs(num))

print("dfs number 6", tree.dfs(6))