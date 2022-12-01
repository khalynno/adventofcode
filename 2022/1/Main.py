with open('input.txt', 'r') as f:
    lines = f.readlines()
    elves = []
    elve_cal = 0
    for line in lines:
        if line.strip() == "":
            elves.append(elve_cal)
            elve_cal = 0

        else:
            current_cal = int(line)
            elve_cal += current_cal
    elves.sort(reverse=True)
    print(max(elves))
    print(elves)
    print(sum(elves[:3]))