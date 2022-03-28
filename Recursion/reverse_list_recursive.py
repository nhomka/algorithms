def reverse_list_recursive(l):
    if len(l) <= 1:
        return l
    return [l[-1]] + reverse_list_recursive(l[:-1])

print(reverse_list_recursive([]))