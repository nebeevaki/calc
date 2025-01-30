def main():
    s = input().split()
    stack(s)


def stack(s):
    st = []
    re = []

    for i in s:
        if i.isdigit():
            re.append(i)
        elif i == "(":
            st.append(i)
        elif i == ")":
            while st and st[-1] != "(":
                re.append(st.pop())
            st.pop()
        else:
            while st and precedence(st[-1]) >= precedence(i):
                re.append(st.pop())
            st.append(i)


    for i in range(len(st) - 1, -1, -1):
        re.append(st.pop(i))


    print(*re)

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0



if __name__ == '__main__':
    main()

