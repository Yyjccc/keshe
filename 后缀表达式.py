def eval_postfix(expr):
    # create an empty stack
    stack = []
    # split the expression by whitespace
    tokens = expr.split()
    # iterate over each token
    for token in tokens:
        # if token is a number
        if token.isdigit():
            # push it to the stack
            stack.append(int(token))
        # if token is an operator
        elif token=='@':
            break
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
expr = input() # read input from user
result = eval_postfix(expr) # evaluate postfix expression
print(result) # print result
