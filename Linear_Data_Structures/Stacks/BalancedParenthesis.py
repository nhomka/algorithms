from Stack import Stack

def par_checker(p_str) -> bool:
    s = Stack()

    for c in p_str:
        if c == "(":
            s.push(c)
        else:
            if s.is_empty():
                return False
            s.pop()
    
    return s.is_empty()

print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False