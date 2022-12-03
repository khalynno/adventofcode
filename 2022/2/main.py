
def checkmatch(in_elf1, in_elf2, s2):
    currentelf1 = in_elf1
    currentelf2 = in_elf2
    print(f"elf1={in_elf1}")
    print(f"elf2={in_elf2}")
    if s2:
        if currentelf2 == "Y":
            match currentelf1 :
                case "A": currentelf2 = "X"
                case "B": currentelf2 = "Y"
                case "C": currentelf2 = "Z"
        elif currentelf2 == "X":
            match currentelf1 :
                case "A": currentelf2 = "Z"
                case "B": currentelf2 = "X"
                case "C": currentelf2 = "Y"
        elif currentelf2 == "Z":
            match currentelf1 :
                case "A": currentelf2 = "Y"
                case "B": currentelf2 = "Z"
                case "C": currentelf2 = "X"

    if currentelf1 == "A":
        if currentelf2 == "Z":
            print("Lost")
            return 3
        elif currentelf2 == "Y":
            print("Won")
            return 6 + 2
        elif currentelf2 == "X":
            print("Draw")
            return 3 + 1
    if currentelf1 == "B":
        if currentelf2 == "X":
            print("Lost")
            return 1
        elif currentelf2 == "Z":
            print("Won")
            return 6 + 3
        elif currentelf2 == "Y":
            print("Draw")
            return 3 + 2
    if currentelf1 == "C":
        if currentelf2 == "Y":
            print("Lost")
            return 2
        elif currentelf2 == "X":
            print("Won")
            return 6 + 1
        elif currentelf2 == "Z":
            print("Draw")
            return 3 + 3


with open('input.txt', 'r') as f:
    lines = f.readlines()
    s1 = 0
    s2 = 0
    for line in lines:
        line.split()
        print(line.split())
        elf1 = line.split()[0]
        elf2 = line.split()[1]
        s1 += checkmatch(elf1, elf2, False)
        s2 += checkmatch(elf1, elf2, True)
    print(f"s1 = {s1}")
    print(f"s2 = {s2}")
