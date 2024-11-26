def longestCommonPrefix(self, strs: List[str]) -> str:
    result = ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i == len(word) or base[i] != word[i]:
                return result
        result += base[i]
    return result
