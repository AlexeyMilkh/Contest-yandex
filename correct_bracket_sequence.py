"""
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить,
является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной. Если A –
правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности,
то последовательность AB – правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no. """


data = input()
stack = []
string = True
if len(data) == 1:
    string = False
elif len(data) == 0:
    string = True
else:
    for i in data:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                string = False
            else:
                open_bracket = stack.pop()
                if open_bracket == '(' and i == ')':
                    continue
                elif open_bracket == '{' and i == '}':
                    continue
                elif open_bracket == '[' and i == ']':
                    continue
                string = False
                break

if string and len(stack) == 0:
    print('yes')
else:
    print('no')
