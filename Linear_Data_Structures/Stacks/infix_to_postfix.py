from Stack import Stack

def infix_to_postfix(infix_str) -> str:
    op_prec = {"(": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}
    op_stack = Stack()
    res = []

    token_list = infix_str.split()
    new_list = [i for j in token_list for i in j]

    for token in new_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            res.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            try:
                popped = op_stack.pop()
            except Exception as error:
                print(f"Invalid Parenthesis: {repr(error)}")
                return
            while popped != "(":
                res.append(popped)
                popped = op_stack.pop()
        elif token in op_prec.keys():
            while not op_stack.is_empty() and op_prec[op_stack.peek()] >= op_prec[token]:
                res.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise RuntimeError(f"Invalid symbol encountered: {token}")
    
    while not op_stack.is_empty():
        res.append(op_stack.pop())

    return ''.join(res)

print(infix_to_postfix(")A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("5 * 3 ^ ( 4 -  2 )"))