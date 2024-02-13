# 21. Дана строка `S` состоящая из открывающихся и закрывающихся скобок '(' и ')'.
# Найти длину наибольшей правильной последовательности скобок.

def _max_correct_braces(s):
    nest = best = best_cnt = start_at = curr = 0
    for i, c in enumerate(s):
        if c == '(':
            curr = 0 # start a new greedy subsubstring
            nest += 1
            continue

        nest -= 1
        curr += 2 # increase the greedy result
        if nest < 0: # currently viewed substring is now invalid, start from scratch
            nest = 0
            curr = 0
            start_at = i+1
            continue

        if nest == 0: # we're at an end of a full substring, let's use its length
            curr = i-start_at+1

        # just compute new answer
        if curr == best:
            best_cnt += 1
        elif curr > best:
            best = max(best, curr)
            best_cnt = 1

    if not best:
        best_cnt = 1

    return best, best_cnt

def max_correct_braces(s):
    m1, c1 = _max_correct_braces(s)
    # consider going from right to left
    m2, c2 = _max_correct_braces(s[::-1].translate(str.maketrans('()', ')(')))
    if m2 > m1:
        return m2, c2
    return m1, c1

s = input()
print(*max_correct_braces(s))