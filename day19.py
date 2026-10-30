import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "scores.txt"
)

print("1. Play Quiz")
print("2. View Past Scores")

choice = input("Enter your choice: ")

if choice == "2":
    print("\n--- Leaderboard ---")

    with open(file_path, "r") as file:
        scores = file.readlines()

    for score_line in scores:
        print(score_line.strip())

elif choice == "1":
    print("Starting quiz...")

else:
    print("Invalid choice!")