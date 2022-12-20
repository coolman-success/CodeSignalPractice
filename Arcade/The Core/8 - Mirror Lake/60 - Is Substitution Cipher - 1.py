def solution(string1, string2):

    func = {}
    for i, ch in enumerate(string1):
        if ch in func and func[ch] != string2[i]:
            return False
        if ch not in func:
            func[ch] = string2[i]
    return len(func.keys()) == len(set(func.values()))
