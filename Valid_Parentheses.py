#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
def valid_parentheses(str):
    a = ["()", "{}", "[]"]
    b = []

    for i in str:
        b.append(i)
        if len(b) > 1 and b[-2] + b[-1] in a:
            b.pop()
            b.pop()

    return b == []

