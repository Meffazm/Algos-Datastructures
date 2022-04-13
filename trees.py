import math


class Node:
    def __init__(self, key=0, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(root, node):
    if root.key > node.key:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

#######################################################


def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_max(root):
    if root.right is None and root.left is None:
        return root.key
    elif root.right is None:
        child_max = tree_max(root.left)
    elif root.left is None:
        child_max = tree_max(root.right)
    else:
        child_max = max(tree_max(root.right), tree_max(root.left))
    return child_max if child_max > root.key else root.key


def _check_BST(root):
    if root.right is None and root.left is None:
        return True, root.key, root.key
    if root.right is None:
        bst, _max, _min = _check_BST(root.left)
        return (root.key >= _max) and bst, max(root.key, _max), min(root.key, _min)
    if root.left is None:
        bst, _max, _min = _check_BST(root.right)
        return (root.key <= _min) and bst, max(root.key, _max), min(root.key, _min)
    (bst_r, _max_r, _min_r), (bst_l, _max_l, _min_l) = _check_BST(root.right), _check_BST(root.left)
    return _max_l <= root.key <= _min_r and bst_l and bst_r, max(root.key, _max_l, _max_r), min(root.key, _min_l, _min_r)


def check_BST(root):
    return _check_BST(root)[0]


def _min_diff(root):
    if root.right is None and root.left is None:
        return math.inf, root.key
    if root.right is None:
        diff, child = _min_diff(root.left)
        return min(diff, abs(root.key - child)), root.key
    if root.left is None:
        diff, child = _min_diff(root.right)
        return min(diff, abs(root.key - child)), root.key
    (diff_r, child_r), (diff_l, child_l) = _min_diff(root.right), _min_diff(root.left)
    return min(diff_l, diff_r, abs(root.key - child_l), abs(root.key - child_r)), root.key


def min_diff(root):
    return _min_diff(root)[0]


def _count_distinct(root):
    if root.right is None and root.left is None:
        return 1, {root.key}
    if root.right is None:
        _, _all = _count_distinct(root.left)
        _all.add(root.key)
        return len(_all), _all
    if root.left is None:
        _, _all = _count_distinct(root.right)
        _all.add(root.key)
        return len(_all), _all
    (_, all_r), (_, all_l) = _count_distinct(root.right), _count_distinct(root.left)
    all_r.update(all_l)
    all_r.add(root.key)
    return len(all_r), all_r


def count_distinct(root):
    return _count_distinct(root)[0]

#################################################


if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(1))
    insert(T, Node(2))
    insert(T, Node(5))
    insert(T, Node(6))
    insert(T, Node(1))
    insert(T, Node(3))
    # should print True
    print(check_BST(T))
    # should print 1
    print(min_diff(T))
    print(count_distinct(T))
