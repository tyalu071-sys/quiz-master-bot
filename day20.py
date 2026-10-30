import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "scores.txt"
)

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        scores = file.readlines()

    for score_line in scores:
        print(score_line.strip())

else:
    print("No scores yet!")