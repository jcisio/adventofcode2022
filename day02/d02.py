f = open(__file__[:-3] + '.in', 'r')


def calculate_score1(lines, points):
    score = 0
    for play in lines:
        x,y = play.split()
        # Your shape score
        score += points[y]
        # Your round score
        if points[x] == points[y]:
            score += 3
        elif points[x] == 1:
            score += 6 if points[y] == 2 else 0
        elif points[x] == 2:
            score += 6 if points[y] == 3 else 0
        else:
            score += 6 if points[y] == 1 else 0
    return score


def calculate_score2(lines, points):
    score = 0
    for play in lines:
        x,y = play.split()
        # Your round score
        score += points[y]
        # Your shape score
        if points[y] == 3:
            score += points[x]
        elif x == 'A':
            score += points['C'] if y == 'X' else points['B']
        elif x == 'B':
            score += points['A'] if y == 'X' else points['C']
        elif x == 'C':
            score += points['B'] if y == 'X' else points['A']
    return score


lines = f.read().strip().split('\n')
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
print("Puzzle 1: ", calculate_score1(lines, points))
points = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
print("Puzzle 2: ", calculate_score2(lines, points))
