import sys

def show(octi):
    for r in range(1, len(octi)-1):
        for c in range (1, len(octi[r])-1):
            print(octi[r][c], end = '')
        print("")

def step(octi):
    octi = [[i+1 for i in r] for r in octi]
    flashed = set()
    prevflash = -1
    while prevflash != len(flashed):
        prevflash = len(flashed)
        for r in range(1, len(octi)-1):
            for c in range (1, len(octi[r])-1):
                if octi[r][c] > 9 and not (r, c) in flashed:
                    octi[r-1][c-1] = octi[r-1][c-1]+1
                    octi[r+1][c+1] = octi[r+1][c+1]+1
                    octi[r-1][c+1] = octi[r-1][c+1]+1
                    octi[r+1][c-1] = octi[r+1][c-1]+1
                    octi[r][c+1] = octi[r][c+1]+1
                    octi[r][c-1] = octi[r][c-1]+1
                    octi[r+1][c] = octi[r+1][c]+1
                    octi[r-1][c] = octi[r-1][c]+1
                    flashed.add((r,c))

    for (r,c) in flashed:
        octi[r][c] = 0

    return (len(flashed) == 100, octi)

def compute(data):
    tiny = -sys.maxsize
    octi = [[tiny] + [int(x) for x in l] + [tiny] for l in data.split('\n')]
    octi.insert(0, [tiny] * len(octi[0]))
    octi.append([tiny] * len(octi[0]))
    show(octi)

    i = 1
    while True:
        (allflash, octi) = step(octi)
        print(i)
        i = i+1
        show(octi)
        if allflash:
            break

test_data1 = """11111
19991
19191
19991
11111"""

test_data2 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

real_data = """5433566276
6376253438
8458636316
6253254525
7211137138
1411526532
5788761424
8677841514
1622331631
5876712227"""

compute(real_data)