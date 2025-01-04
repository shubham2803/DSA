# https://runestone.academy/ns/books/published/pythonds/Trees/SearchTreeImplementation.html
class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent.left_child == self

    def is_right_child(self):
        return self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return self.right_child is None and self.left_child is None

    def has_any_children(self):
        return self.right_child is not None or self.left_child is not None

    def has_both_children(self):
        return self.right_child is not None and self.left_child is not None

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self


class BinaryTree:
    def __init__(self):
        self.root: (TreeNode or None) = None
        self.size = 0

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return self._get(item, self.root) is not None

    def __delitem__(self, key):
        self.delete(key)

    def _put(self, key, val, current_node):
        if key > current_node.key:
            if current_node.has_right_child():
                self._put(key, val, current_node)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_left_child():
                self._put(key, val, current_node)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key > current_node.key:
            return self._get(key, current_node.right_child)
        else:
            return self._get(key, current_node.left_child)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        return None

    def remove(self, target_node):
        pass

    def delete(self, key):
        if self.size > 1:
            target_node = self._get(key, self.root)
            if target_node:
                self.remove(target_node)
                self.size -= 1
            else:
                raise KeyError(f'{key} key not present in tree.')
        elif self.size == 1 and self.root.key == key:
            self.remove(key)
            self.size -= 1
        else:
            raise KeyError(f'{key} key not present in tree.')
