def solution(inputString):
    
    stack = []
    s = inputString
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            temp = s[stack[-1]:i + 1]
            s = s[:stack[-1]] + temp[::-1] + s[i + 1:]
            stack.pop()
    
    return ''.join(ch for ch in s if ch != '(' and ch != ')')
