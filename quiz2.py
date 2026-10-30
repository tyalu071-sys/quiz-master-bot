import os

questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Capital of Japan?", "answer": "Tokyo"},
    {"question": "How many days in a week?", "answer": "7"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What colour is the sky?", "answer": "blue"},
    {"question": "How many months are in a year?", "answer": "12"},
    {"question": "What is 10 - 4?", "answer": "6"},
    {"question": "Which planet do we live on?", "answer": "Earth"}
]

player = input("What is your name? ")
score = 0

for number, item in enumerate(questions, start=1):
    print("\nQuestion", number, "of", len(questions))
    user_answer = input(item["question"] + " ")

    if user_answer.strip().lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong. The answer was", item["answer"])

print("\nQuiz over! You scored", score, "out of", len(questions))

if score == len(questions):
    print("Perfect score! Amazing!")
elif score >= len(questions) / 2:
    print("Good job!")
else:
    print("Keep practising!")

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "scores.txt"
)

with open(file_path, "a") as file:
    file.write(
        player + " scored " + str(score)
        + " out of " + str(len(questions)) + "\n"
    )

print("Your  result has been saved!")
print("\n--- Past Scores ---")

with open(file_path, "r") as file:
    scores = file.readlines()

for score_line in scores:
    print(score_line.strip())