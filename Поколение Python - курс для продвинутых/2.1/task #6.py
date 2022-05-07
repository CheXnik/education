x = [a for a in input()]

if len(x) < 6: print(int("".join(x[::-1])))
else: print(f'{x[0]}{"".join(x[:0:-1])}')
