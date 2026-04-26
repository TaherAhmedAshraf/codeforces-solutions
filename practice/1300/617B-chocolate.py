bars = int(input())
pieces = input()
nuts = pieces.count('1')

if(nuts < 2):
    print(nuts)
else:
    pos_of_1 = []
    for _idx, n in enumerate(pieces.split()):
        if n == "1":
            pos_of_1.append(_idx)
    
    possibility = 1
    for _idx, pos in enumerate(pos_of_1):
        if(nuts -1 != _idx):
            zeros_between_pos = pos_of_1[_idx + 1] - pos
            if(zeros_between_pos != 0):
                possibility = possibility*zeros_between_pos
    print(possibility)