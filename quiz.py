questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Capital of Japan?", "answer": "Tokyo"},
    {"question": "How many days in a week?", "answer": "7"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "Which planet do we live on?", "answer": "Earth"},
    {"question": "What colour is the sky?", "answer": "Blue"},
    {"question": "How many months are in a year?", "answer": "12"},
    {"question": "What is 10 - 4?", "answer": "6"}
]

score = 0

for number, item in enumerate(questions, start=1):
    print(f"\nQuestion {number} of {len(questions)}")
    
    user_answer = input(item["question"] + " ")
    user_answer = user_answer.strip().lower()

    if user_answer == item["answer"].lower():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong. The answer was", item["answer"])

print("\nQuiz over! You scored", score, "out of", len(questions))

if score == len(questions):
    print("Perfect score! Amazing!")
elif score >= len(questions) / 2:
    print("Good job!")
else:
    print("Keep practising - you will get there!")