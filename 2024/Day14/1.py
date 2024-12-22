import matplotlib.pyplot as plt
import numpy as np

def parse_input():
    with open("2024/Day14/input.txt", 'r') as file:
        inp = file.readlines()

    lines = []
    for line in inp:
        line = line.split()
        line[0] = line[0].replace('p=', '')
        line[1] = line[1].replace('v=', '')
        line[0] = line[0].split(',')
        line[1] = line[1].split(',')
        lines.append(line)

    return lines

def get_pos(x, y, v_x, v_y, seconds, tiles_tall, tiles_wide):
    x = (x + v_x*seconds) % tiles_tall
    y = (y + v_y*seconds) % tiles_wide
    return (x, y)

def main():
    lines = parse_input()
    tiles_wide = 101
    tiles_tall = 103

    pos = []
    quad1 = []
    quad2 = []
    quad3 = []
    quad4 = []
    tall = tiles_tall // 2
    wide = tiles_wide // 2

    for line in lines:
        y, x = line[0]
        v_y, v_x = line[1]
        x, y = get_pos(int(x), int(y), int(v_x), int(v_y), 100, tiles_tall, tiles_wide)
        pos.append((x, y))

    # print(pos)

    for p in pos:
        x, y = p[0], p[1]
        if x < tall and y < wide:
            quad1.append(pos)
        if x >= (tiles_tall - tall) and y < wide:
            quad2.append(pos)
        if x < tall and y >= (tiles_wide-wide):
            quad3.append(pos)
        if x >= (tiles_tall - tall) and y >= (tiles_wide-wide):
            quad4.append(pos)

    res = len(quad1) * len(quad2) * len(quad3) * len(quad4)
    print("Part 1:", res)

    for seconds in range(7600, 7700):
        posx = []
        posy = []
        
        for line in lines:
            y, x = line[0]
            v_y, v_x = line[1]
            x, y = get_pos(int(x), int(y), int(v_x), int(v_y), seconds, tiles_tall, tiles_wide)
            posx.append(x)
            posy.append(y)

        plt.scatter(np.array(posx), np.array(posy), color='green')
        plt.savefig(f"2024/Day14/{seconds}.png")
        plt.clf()

    print("Part 2:", 7672, "by analysing the images.")

main()