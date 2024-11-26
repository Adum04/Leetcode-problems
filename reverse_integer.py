def reverse(self, x: int) -> int:
    n = 1 if x >= 0 else -1
    y = str(abs(x))
    cha = ""
    for i in y:
        cha = i + cha
    z = int(n * int(cha))
    if z < -(1 << 31) or z > (1 << 31) - 1:
        return 0
    return z
