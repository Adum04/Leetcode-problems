def plusOne(self, digits: List[int]) -> List[int]:
    st = ""
    for i in digits:
        st = st + str(i)
    result = str(int(st) + 1)
    x = list(result)
    int_list = list(map(int, x))
    return int_list
