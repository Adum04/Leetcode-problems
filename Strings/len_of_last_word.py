def lengthOfLastWord(self, s: str) -> int:
    lst = s.split()
    last = lst[-1]
    return len(last)
