from stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stck = Stack()
    postfixList = []
    tokenList = infixexpr.split() #splits by space

    for token in tokenList:
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            op_stck.push(token)
        elif token == ')':
            topToken = op_stck.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = op_stck.pop()
        else:
            while (not op_stck.isEmpty()) and \
               (prec[op_stck.peek()] >= prec[token]):
                  postfixList.append(op_stck.pop())
            op_stck.push(token)
        print("--")
        for i in op_stck.items:
            print(i)
        print(postfixList)
    while not op_stck.isEmpty():
        postfixList.append(op_stck.pop())
    return " ".join(postfixList)
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

# print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
