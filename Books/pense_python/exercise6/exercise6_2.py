
def ackermann(m, n):
    if m == 0:
        n += 1
        return n
    if m > 0 and n == 0:
        return ackermann(m -1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n -1))

print(ackermann(3,4))
