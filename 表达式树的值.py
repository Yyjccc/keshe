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
def traveltree(tree,output):
    s=tree.data
    #若是运算符先打印‘（’
    if s in '+-*/':
        output.append('(')
    #若左子树存在递归遍历
    if tree.left:
        output=traveltree(tree.left,output)
    #将当前压入结果
    output.append(tree.data)
    # 若右子树存在递归遍历
    if tree.right:
        output=traveltree(tree.right,output)
    #若是运算符最后打印‘）’
    if s in '+-*/':
        output.append(')')
    return output

import sys
from collections import deque

# 返回给定运算符的优先级。
def prec(c):
    # 乘除法
    if c == '*' or c == '/':
        return 3
    # 加减法
    if c == '+' or c == '-':
        return 4
    # 根据需要添加更多操作员
    return sys.maxsize  # 用于左括号 '('

# 用于检查给定令牌是否为操作数
def isoperand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')


# 将中缀表达式转换为后缀表达式的函数。
def infixToPostfix(fix):
    if not fix or not len(fix):
        return True
    # 创建一个空Stack来存储算子
    s = deque()
    # 创建一个字符串来存储后缀表达式
    postfix = []
    # 从左到右处理中缀表达式
    for c in fix:
        # 如果当前token是一个左括号'('，将其推入栈
        if c == '(':
            s.append(c)
        #  如果当前标记是右括号')'
        elif c == ')':
            # 从Stack栈中弹出直到对应的左括号'('
            # 被移除。将每个运算符附加到后缀表达式的末尾
            while s[-1] != '(':
                postfix.append( s.pop())
            s.pop()

        #  如果当前是一个操作数，则将其附加在操作数的末尾
        # 后缀表达式
        elif isoperand(c):
            postfix.append(c)

        else:
            # 从Stack栈中删除具有更高或相等优先级的运算符
            # 并将它们附加在后缀表达式的末尾
            while s and prec(c) >= prec(s[-1]):
                postfix.append(s.pop())
            # 最后，将当前压入Stack顶
            s.append(c)
    # 在后缀表达式的末尾附加Stack栈中任何剩余的运算符
    while s:
        postfix.append(s.pop())
    # 返回后缀表达式
    return postfix

#定义计算后缀表达式的函数
def eval_postfix(tokens):
    stack = []
    # split the expression by whitespace
    # iterate over each token
    for token in tokens:
        # if token is a number
        if token.isdigit():
            # push it to the stack
            stack.append(int(token))
        # if token is an operator
        else:
            # pop two operands from the stack
            op2 = stack.pop()
            op1 = stack.pop()
            # apply the operator on them
            if token == "+":
                result = op1 + op2
            elif token == "-":
                result = op1 - op2
            elif token == "*":
                result = op1 * op2
            elif token == "/":
                result = op1 // op2 # use integer division
            # push the result back to the stack
            stack.append(result)
    # return the final result from the stack
    return stack.pop()

def main():
    # 循环输入
    while True:
        try:
            # 将输入字符串转化为列表
            str = input()
            nodelist = []
            out=[]
            res=''
            # 创建二叉树
            nodelist = str.split()

            tree = create_tree(nodelist)
            cnt=traveltree(tree, out)
            forcnt=infixToPostfix(cnt)
            s=eval_postfix(forcnt).__str__()
            res=res.join(cnt)
            res=res+'='+s
            print(res)
        except EOFError:
            # 到达 EOF 时中断循环
            break

if __name__=='__main__':
    main()