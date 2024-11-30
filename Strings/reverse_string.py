def reverseString(self, s: List[str]) -> None:
    n = len(s)
    first = 0
    last = n - 1
    # mid = n//2
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1
