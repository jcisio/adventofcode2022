from pprint import pprint


f = open(__file__[:-3] + '.in', 'r')


def get_dir(fs, path):
    dir = fs
    for p in path:
        dir = dir['children'][p]
    return dir


def get_size(dir):
    # Cache
    if dir['size'] == -1:
        dir['size'] = sum([get_size(dir['children'][child]) for child in dir['children']])
    return dir['size']


def parse_fs(lines):
    fs = {
        'dir': True,
        'name': '/',
        'size': -1,
        'children': {}
    }
    current_path = []
    current_dir = fs
    line = lines.pop(0)
    line = lines.pop(0)
    while lines:
        #print(line)
        #pprint(fs)
        if line[0] == '$':
            if line[2:] == 'ls':
                #pprint(current_path), pprint(current_dir)
                while lines:
                    line = lines.pop(0)
                    #print(line)
                    if line[0] != '$':
                        size, name = line.split()
                        item = {
                            'dir': size == 'dir',
                            'name': name,
                            'size': -1 if size == 'dir' else int(size),
                            'children': {}
                        }
                        current_dir['children'][name] = item
                    else:
                        break
            else:
                dir = line.split()[2]
                if dir == '..':
                    current_path.pop()
                else:
                    current_path.append(dir)
                current_dir = get_dir(fs, current_path)
                line = lines.pop(0)
    get_size(fs)
    return fs


def sum_size_less_than(dir, max_size):
    size = 0
    if not dir['dir']: return 0
    if dir['size'] <= max_size:
        size += dir['size']
    for d in dir['children']:
        size += sum_size_less_than(dir['children'][d], max_size)
    return size


def solve(fs):
    return sum_size_less_than(fs, 100000)


fs = parse_fs(f.read().strip().split('\n'))
print("Puzzle 1: ", solve(fs))
