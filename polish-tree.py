class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


operators = {'+', '-', '*', '/'}

def polish_to_tree(polish: list[str], i=0) -> tuple[Node, int]:
    token = polish[i]
    node = Node(token)
    if token in operators:
        node.left, i = polish_to_tree(polish, i+1)
        node.right, i = polish_to_tree(polish, i)
        return node, i
    else:
        return node, i+1


def pre_walk(tree: Node) -> None:
    if tree is None: return
    print(tree.val, end=' ')
    pre_walk(tree.left)
    pre_walk(tree.right)


def order_walk(tree: Node) -> None:
    if tree is None: return
    operator = tree.val in operators
    if operator:
        print('(', end='')
    order_walk(tree.left)
    print(tree.val, end=' ')
    order_walk(tree.right)
    if operator:
        print(')', end='')


def post_walk(tree: Node) -> None:
    if tree is None: return
    post_walk(tree.left)
    post_walk(tree.right)
    print(tree.val, end=' ')


polish = ['+', '1', '*', '2', '-', '3', '/', '4', '5']

expression_tree, len_read = polish_to_tree(polish)
assert len_read == len(polish)

print('Polish:')
pre_walk(expression_tree)

print('\n\nInfix:')
order_walk(expression_tree)

print('\n\nReverse polish:')
post_walk(expression_tree)
print()
