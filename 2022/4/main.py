with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    s1 = 0
    s2 = 0
    for line in lines:
        left, right = line.split(',')[0], line.split(',')[1]
        print(left, right)
        x1, x2, y1, y2 = int(left.split('-')[0]), int(left.split('-')[1]), int(right.split('-')[0]), int(right.split('-')[1])
        print(f"x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}")
        if x1 <= y1 and x2 >= y2 or y1 <= x1 and y2 >= x2:
            s1 += 1
        if y1 <= x2 and y2 >= x1:
            s2 += 1

    print(s1)
    print(s2)