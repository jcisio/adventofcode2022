f = open(__file__[:-3] + '.in', 'r')


def add_pixels(pixels, v, current, cycles):
    for _ in range(cycles):
        current = (current + 1) % 40
        pixels.append('#' if v - 1 <= current - 2 <= v + 1 else '.')


def solve(lines):
    start, steps, count = 20, 40, 6
    v, s, cycle, next = 1, 0, 1, start
    pixels = []
    for line in lines:
        ins = line.split()
        cycles = 1 if ins[0] == 'noop' else 2
        add_pixels(pixels, v, cycle, cycles)
        cycle += cycles
        if cycle > next:
            s += v * next
            next += steps
        if next > steps * (count+1):
            break
        if ins[0] == 'addx':
            v += int(ins[1])
    for i in range(count):
        print(''.join(pixels[i*40:(i+1)*40]))
    return s


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solve(lines))
