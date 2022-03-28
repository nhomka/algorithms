def int_to_str(n, base):
    chars = "0123456789ABCDEF"

    if n < base:
        return chars[n]
    else:
        return int_to_str(n // base, base) + chars[n % base]

print(int_to_str(1453, 16))
print(int_to_str(10, 2))