file = open("scores.txt", "r")

scores = file.readlines()

print("\n--- Previous Scores ---")

for score in scores:
    print(score.strip())

file.close()

print("\nLeaderboard data displayed successfully!")
