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
    postfix = ''
    # 从左到右处理中缀表达式
    for c in infix:
        # 如果当前token是一个左括号'('，将其推入栈
        if c == '(':
            s.append(c)
        #  如果当前标记是右括号')'
        elif c == ')':
            # 从Stack栈中弹出直到对应的左括号'('
            # 被移除。将每个运算符附加到后缀表达式的末尾
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()

        #  如果当前是一个操作数，则将其附加在操作数的末尾
        # 后缀表达式
        elif isoperand(c):
            postfix += c

        else:
            # 从Stack栈中删除具有更高或相等优先级的运算符
            # 并将它们附加在后缀表达式的末尾
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
            # 最后，将当前压入Stack顶
            s.append(c)
    # 在后缀表达式的末尾附加Stack栈中任何剩余的运算符
    while s:
        postfix += s.pop()
    # 返回后缀表达式
    return postfix


if __name__ == '__main__':
    infix = input()
    postfix = infixToPostfix(infix)
    print(postfix)