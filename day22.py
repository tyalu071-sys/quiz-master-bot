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
    questions = quiz_bank[chosen_category]

    print("\nYou selected:", chosen_category)

    for item in questions:
        print(item["question"])
else:
    print("Invalid category!")    