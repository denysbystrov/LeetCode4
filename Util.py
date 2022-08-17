from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next_n=None):
        self.val = val
        self.next = next_n


def create_tree_from_dict(root_num: int, node_dict: dict):
    if root_num is None:
        return None
    root_node = TreeNode(root_num)
    queue = [root_node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        left_num, right_num = node_dict[current_node.val][0], node_dict[current_node.val][1]
        if left_num is not None:
            left_node = TreeNode(left_num)
            current_node.left = left_node
            queue.append(left_node)
        if right_num is not None:
            right_node = TreeNode(right_num)
            current_node.right = right_node
            queue.append(right_node)

    return root_node


def create_tree_from_array(array: List) -> TreeNode:
    tree = []
    for num in array:
        new_node = TreeNode(num)
        tree.append(new_node)

    for i in range(len(array)):
        left_child_index = i*2 + 1
        right_child_index = i*2 + 2
        tree[i].left = tree[left_child_index] if left_child_index < len(tree) else None
        tree[i].right = tree[right_child_index] if right_child_index < len(tree) else None

    if len(tree) > 0:
        return tree[0]
    else:
        return None


def check_tree_height_balanced(root: TreeNode):
    if root is None:
        return 0

    height_left = check_tree_height_balanced(root.left)
    height_right = check_tree_height_balanced(root.right)

    if height_left is None or height_right is None:
        return None
    elif abs(height_left-height_right) <= 1:
        return 1+max(height_left, height_right)
    else:
        return None


def create_list_from_array(arr, cycle_index):
    linked_list = [ListNode(num) for num in arr]
    for i in range(len(arr)-1):
        linked_list[i].next = linked_list[i+1]
    if cycle_index != -1:
        linked_list[-1].next = linked_list[cycle_index]

    return linked_list[0] if len(arr) > 0 else None


def create_two_lists(arr_a, arr_b, intersection_idx):
    linked_list_a = [ListNode(num) for num in arr_a]
    linked_list_b = [ListNode(num) for num in arr_b]
    return_val = None
    for i in range(len(arr_a)-1):
        linked_list_a[i].next = linked_list_a[i+1]

    for i in range(len(arr_b)-1):
        linked_list_b[i].next = linked_list_b[i+1]

    if intersection_idx != -1:
        linked_list_b[-1].next = linked_list_a[intersection_idx]
        return_val = linked_list_a[intersection_idx]

    head_a = linked_list_a[0] if len(linked_list_a) > 0 else None
    head_b = linked_list_b[0] if len(linked_list_b) > 0 else None
    return head_a, head_b, return_val


def convert_list_to_array(node: ListNode) -> list:
    num_array = []
    current_node = node
    while current_node:
        num_array.append(current_node.val)
        current_node = current_node.next

    return num_array


def check_two_arrays_equal(arr1: List[int], arr2: List[int]) -> bool:
    return sorted(arr1) == sorted(arr2)


def is_palindrome(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
    return True