print("=" * 40)
print("       WELCOME TO QUIZ MASTER BOT")
print("=" * 40)

print("Test your knowledge and have fun!")
print("Choose your category and start playing.")

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
    exit()

print("\n" + "=" * 40)
print("           QUIZ COMPLETED!")
print("=" * 40)

print("Category:", chosen_category)
print("Your final score:", score)

rank = 1
if score < 7:
    rank = 2
print("Your rank:", rank)

print("=" * 40)
print("       THANK YOU FOR PLAYING!")
print("=" * 40)    