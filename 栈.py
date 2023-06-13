# 定义逻辑联结词和优先级
operators = {"!": 4, "^": 3, "||": 2, "->": 1, "<->": 0}
# 定义逻辑运算的函数
def negate(a):
    return 0 if a else 1

def conjunct(a, b):
    return a and b

def disjunct(a, b):
    return a or b

def imply(a, b):
    return not a or b

def equiv(a, b):
    return a == b

# 定义一个栈类
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# 定义一个词法分析的函数，将逻辑表达式分隔为多个词
def tokenize(expr):
    tokens = []
    variables = set()
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.islower(): # 如果是小写字母，就是一个逻辑变量
            tokens.append(c)
            variables.add(c)
            i += 1
        elif c in operators or c in "()": # 如果是逻辑联结词或括号，就是一个词
            tokens.append(c)
            i += 1
        elif c == " ": # 如果是空格，就忽略它
            i += 1
        else: # 否则就是一个错误的字符
            raise ValueError("Invalid character: " + c)
    return tokens, sorted(variables)

# 定义一个真值表生成的函数，计算逻辑表达式在每一个逻辑变量取值组合下的值
def truth_table(expr):
    tokens, variables = tokenize(expr) # 对表达式进行词法分析
    n = len(variables) # 变量的个数
    m = 2 ** n # 取值组合的个数
    table = [[0] * (n + 1) for _ in range(m)] # 初始化真值表为全零矩阵
    for i in range(m): # 遍历每一种取值组合
        values = bin(i)[2:].zfill(n) # 将i转换为二进制字符串，表示变量的取值
        for j in range(n): # 遍历每一个变量
            table[i][j] = int(values[j]) # 将变量的取值存入真值表中
        stack = Stack() # 创建一个栈来存储和计算表达式的值
        for token in tokens: # 遍历每一个词
            if token.islower(): # 如果是变量，就将其对应的值压入栈中
                stack.push(table[i][variables.index(token)])
            elif token == "!": # 如果是否定，就对栈顶元素进行否定运算，并将结果压入栈中
                stack.push(negate(stack.pop()))
            elif token == "^": # 如果是合取，就对栈顶两个元素进行合取运算，并将结果压入栈中
                stack.push(conjunct(stack.pop(), stack.pop()))
            elif token == "||": # 如果是析取，就对栈顶两个元素进行析取运算，并将结果压入栈中
                stack.push(disjunct(stack.pop(), stack.pop()))
            elif token == "->": # 如果是蕴涵，就对栈顶两个元素进行蕴涵运算，并将结果压入栈中
                stack.push(imply(stack.pop(), stack.pop()))
            elif token == "<->": # 如果是等值，就对栈顶两个元素进行等值运算，并将结果压入栈中
                stack.push(equiv(stack.pop(), stack.pop()))
            elif token == "(": # 如果是左括号，就压入栈中
                stack.push(token)
            elif token == ")": # 如果是右括号，就弹出栈中的元素，直到遇到左括号
                while not stack.is_empty() and stack.top() != "(":
                    stack.pop()
                if not stack.is_empty() and stack.top() == "(":
                    stack.pop()
        table[i][n] = stack.pop() # 最后栈中剩下的唯一元素就是表达式的值，将其存入真值表中
    return table, variables

# 定义一个输出格式化的函数，按要求输出词和真值表
def format_output(expr):
    tokens, variables = tokenize(expr) # 对表达式进行词法分析
    table, variables = truth_table(expr) # 生成真值表
    print(" ".join(tokens)) # 输出词，用空格分隔
    print(" ".join(variables)) # 输出变量，用空格分隔
    for row in table: # 输出真值表，每一行用空格分隔
        print(" ".join(map(str, row)))

# 主函数，循环读取输入，并输出结果
def main():
    while True:
        try:
            expr = input() # 读取输入
            format_output(expr) # 输出结果
        except EOFError: # 如果遇到文件结束符，就退出循环
            break

# 调用主函数
main()
