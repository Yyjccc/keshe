# 定义树节点的一个类
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 定义递归创建二叉树函数，传入节点列表
def create_tree(li):
    #节点不为空，弹出列表中第一个元素,并赋给s
    if li:
        s=li.pop(0)
    # 若s为#,则跳过
        if s == "#":
            return None
        # 否则创建树节点
        node = Node(s)
        # 递归创建左右子树
        node.left = create_tree(li)
        node.right = create_tree(li)
        # 返回节点
        return node
    else:
        return None

# 定义一个函数，以中序遍历的方式递归打印树
def print_tree(node, flag):
    # 节点不为空
    if node:
        # 递归打印带有增加标志的右子树
        print_tree(node.right, flag + 1)
        # 根据flag打印一些空格，然后打印节点数据
        print(" " * (4 * (flag-1)), end="")
        print(node.data)
        # 递归打印带有增加标志的左子树
        print_tree(node.left, flag + 1)

# 使用 while 循环读取输入，直到引发 EOFError
while True:
    try:
        # 创建列表，将输入字符串转化成列表
        str=input()
        nodelist=[]
        nodelist=str.split()

        tree = create_tree(nodelist)
        # 打印初始标志为 1 的中序遍历树
        print_tree(tree, 1)
        # 打印空行
        print()
    except EOFError:
        # 到达 EOF 时中断循环
        break
