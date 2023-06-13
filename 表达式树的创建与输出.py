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

#定义中序循环遍历，并打印表达式的函数
def tra_print(tree,output):
    s=tree.data
    #若是运算符先打印‘（’
    if s in '+-*/':
        output+='('
    #若左子树存在递归遍历
    if tree.left:
        output=tra_print(tree.left,output)
    #将当前压入结果
    output+=tree.data
    # 若右子树存在递归遍历
    if tree.right:
        output=tra_print(tree.right,output)
    #若是运算符最后打印‘）’
    if s in '+-*/':
        output+=')'
    return output

#循环输入
while True:
    try:
        #将输入字符串转化为列表
        str=input()
        nodelist=[]
        #创建二叉树
        nodelist=str.split()
        #打印结果
        tree = create_tree(nodelist)
        print(tra_print(tree,''))
    except EOFError:
        # 到达 EOF 时中断循环
        break