import sys

while True:
    text = sys.stdin.readline().rstrip()
    stack = []
    is_true = True
    if text == '.':
        break
    else:
        for word in text:
            if word == '(':
                stack.append('(')
            elif word == '[':
                stack.append('[')
            elif word == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    is_true = False
                    break
            elif word == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    is_true = False
                    break

        if len(stack) == 0 and is_true:
            print('yes')
        else:
            print('no')

