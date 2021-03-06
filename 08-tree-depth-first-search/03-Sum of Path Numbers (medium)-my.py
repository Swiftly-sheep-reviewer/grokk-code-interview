class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here
    sum = [0]

    def dfs(node, path_sum):
        if node is None:
            return
        path_sum = path_sum * 10 + node.val
        if node.left is None and node.right is None:
            sum[0] += path_sum
        dfs(node.left, path_sum)
        dfs(node.right, path_sum)
        # path_sum = path_sum // 10

    dfs(root, 0)
    return sum[0]


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
