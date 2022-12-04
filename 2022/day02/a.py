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

X, Y, Z = 1, 2, 3
lost, draw, won = 0, 3, 6

for line in lines:
    match line.strip():
        case 'A X': score += X + draw
        case 'A Y': score += Y + won
        case 'A Z': score += Z + lost
        case 'B X': score += X + lost
        case 'B Y': score += Y + draw
        case 'B Z': score += Z + won
        case 'C X': score += X + won
        case 'C Y': score += Y + lost
        case 'C Z': score += Z + draw
print(score)
