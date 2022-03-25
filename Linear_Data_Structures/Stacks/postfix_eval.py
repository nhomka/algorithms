from Stack import Stack

def op_eval(b, a, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b

def postfix_eval(eval_str) -> float:
    operand_stack = Stack()

    for i in eval_str.split():
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            operand_stack.push(i)
        else:
            operand_stack.push(op_eval(float(operand_stack.pop()), float(operand_stack.pop()), i))
    
    return operand_stack.pop()

print(postfix_eval("7 8 + 3 2 + /"))
