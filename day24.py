quiz_bank = {
    "Maths": [
        {"question": "2 + 2?", "answer": "4"},
        {"question": "10 - 3?", "answer": "7"}
    ],
    "Geography": [
        {"question": "Capital of Japan?", "answer": "Tokyo"}
    ]
}

print("Categories available:")
for name in quiz_bank:
    print("-", name)

chosen_category = input("Choose a category: ")

if chosen_category in quiz_bank:

    difficulty = input("Choose difficulty (Easy/Hard): ").lower()

    if difficulty == "easy":
        points = 1
    elif difficulty == "hard":
        points = 2
    else:
        print("Invalid difficulty!")
        exit()

    score = 0

    questions = quiz_bank[chosen_category]

    for item in questions:
        print(item["question"])
        answer = input("Your answer: ")

        if answer.strip().lower() == item["answer"].lower():
            print("Correct!")
            score += points
        else:
            print("Wrong!")

    print("Your final score:", score)

else:
    print("Invalid category!")