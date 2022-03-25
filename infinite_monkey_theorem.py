import random

def generate_sequence(match, best_res):
    chars = " abcdefghijklmnopqrstuvwxyz"
    seq = ['0']*len(match) if best_res == None else [c for c in best_res]
    for i in range(len(match)):
        if seq[i] != match[i]:
                seq[i] = chars[random.randrange(0, 27)]
    return ''.join(seq)

def check_sequence(sequence, match):
    score = 0
    for i in range(len(sequence)):
        if sequence[i]==match[i]:
            score += 1
    return (True, score) if score == len(sequence) else (False, score)

def main(match):
    finished, count, best, best_res = False, 0, 0, None
    
    while not finished:
        sequence = generate_sequence(match, best_res)
        finished, score = check_sequence(sequence, match)
        count += 1
        if score > best:
            best_res = sequence
            best = score
        #print(count, sequence)
        if count % 1000 == 0:
            print(count, sequence, best)
    print(sequence, count)

if __name__ == "__main__":
    main("methinks it is like a weasel")