def rotateString(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    stri = s + s
    for i in stri:
        if goal in stri:
            return True
    return False
