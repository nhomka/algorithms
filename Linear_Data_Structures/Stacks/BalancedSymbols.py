from Stack import Stack

def balance_checker(p_str) -> bool:
    s = Stack()

    for c in p_str:
        if c in "([{":
            s.push(c)
        else:
            if s.is_empty():
                return False
            open = s.pop()
            if open+c not in ["()", "{}", "[]"]:
                return False
    
    return s.is_empty()

print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))