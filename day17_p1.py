import sys

def check(v, t):
    ((xb, xt), (yb, yt)) = t
    (vx, vy) = v
    x, y = (0, 0)

    max_y = 0

    while y >= yb and x <= xt:
        if x >= xb and x <= xt and y >= yb and y <= yt:
            return True, max_y

        x = x + vx
        y = y + vy
        vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
        vy = vy - 1
        if y > max_y:
            max_y = y

    return (False, None)

def compute(data):
    # print(check((6,9), data))

    ((xb, xt), (yb, yt)) = data
    max_x = xt+1
    min_x = 0
    max_y = -(yb-1)
    min_y = yb-1
    print(f'checking x={min_x}..{max_x} y={min_y}..{max_y}')

    hv = None
    highest = -sys.maxsize

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            (c, h) = check((x, y), data)
            if c and h > highest:
                highest = h
                hv = (x, y)


    print(highest)
    print(hv)


# 
test_data=((20, 30), (-10, -5))

# target area: x=79..137, y=-176..-117
data=((79, 137), (-176, -117))

compute(data)