from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for _line in lines:
        if pattern in _line:
            yield _line, previous_lines
        previous_lines.append(_line)


# use example
if __name__ == 'main':
    with open('some_file.txt') as f:
        for line, prev_lines in search(f, 'python', 5):
            for p_line in prev_lines:
                print(p_line, end='')
            print(line, end='')
            print('-'*20)
