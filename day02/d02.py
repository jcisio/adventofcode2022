f = open(__file__[:-3] + '.in', 'r')


def calculate_score(lines, points):
    score = 0
    for play in lines:
        x,y = play.split()
        # Your shape score
        score += points[y]
        # Your result score
        if points[x] == points[y]:
            score += 3
        elif points[x] == 1:
            score += 6 if points[y] == 2 else 0
        elif points[x] == 2:
            score += 6 if points[y] == 3 else 0
        else:
            score += 6 if points[y] == 1 else 0
    return score


lines = f.read().strip().split('\n')
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
score = calculate_score(lines, points)
print("Puzzle 1: ", score)
