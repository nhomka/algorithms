from Stack import Stack

def convert_from_base_10(num, base):
    s = Stack()
    digits = "0123456789ABCDEF"

    while num > 0:
        s.push(num % base)
        num //= base
    
    return (''.join([digits[s.pop()] for _ in range(s.size())]))

print(convert_from_base_10(25, 2))
print(convert_from_base_10(26, 16))