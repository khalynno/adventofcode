def find_same_char(in_left, in_right):
    return (list(set(in_left)&set(in_right)))

def find_tree(in_first, in_second, in_third):
    return (list(set(in_first)&set(in_second)&set(in_third)))

def calculate_char_value(char):
    if ord(char) >= ord('a'):

        return ord(char) - ord('a') + 1
    else:

        return ord(char) - ord('A') + 27

def s1(in_data):
    s1 = 0
    for line in in_data:
        left, right = line[:len(line)//2], line[len(line)//2:]

        s1 += calculate_char_value(find_same_char(left, right)[0])
    print(s1)


def s2(in_data: str):
    s2 = 0
    for i in range(0, len(in_data), 3):
        x = i
        chunk = in_data[x:x+3]
        s2 += calculate_char_value(find_tree(chunk[0], chunk[1], chunk[2])[0])
    print(s2)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    s1(lines)
    s2(lines)