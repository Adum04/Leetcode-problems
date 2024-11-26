def divide(self, dividend: int, divisor: int) -> int:
    if divisor != 0:
        divider = int(dividend / divisor)
    if divider >= (1 << 31) - 1:
        divider = (1 << 31) - 1
    if divider <= -(1 << 31) - 1:
        divider = -(1 << 31) - 1
    return divider
