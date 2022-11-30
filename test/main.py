with open('input.txt', 'r') as f:
    Lines = f.readlines()
    Lastnumber = int(Lines[0].strip())
    Result = 0
    for line in Lines:
        if Lastnumber < int(line.strip()):
            print(f"increase {int(line.strip())}")
            Result += 1
        Lastnumber = int(line.strip())
    print(f"Resultat = {Result}")