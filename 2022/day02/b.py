with open("a.txt", "r") as f:
    lines = f.readlines()

score = 0
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# part B:
# second column says how the round needs to end:
# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win.

X, Y, Z = 1, 2, 3
lost, draw, won = 0, 3, 6

for line in lines:
    match line.strip():
        case 'A X': score += lost + Z
        case 'A Y': score += draw + X
        case 'A Z': score += won + Y
        case 'B X': score += lost + X
        case 'B Y': score += draw + Y
        case 'B Z': score += won + Z
        case 'C X': score += lost + Y
        case 'C Y': score += draw + Z
        case 'C Z': score += won + X
print(score)
