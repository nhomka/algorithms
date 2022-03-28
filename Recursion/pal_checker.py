def is_pal(s):
    valid = "abcdefghijklmnopqrstuvwxyz"
    stripped = ''.join([i for i in s if i in valid])

    def compare(s):
        if len(s) <= 1:
            return True
        else:
            return (s[0] == s[-1]) and compare(s[1:-1])

    return compare(stripped)

print(is_pal("ho"))