def isAnagram(self, s: str, t: str) -> bool:
    hash_map = {}
    hashy = {}
    for i in s:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for j in t:
        if j in hashy:
            hashy[j] += 1
        else:
            hashy[j] = 1
    return hash_map == hashy
