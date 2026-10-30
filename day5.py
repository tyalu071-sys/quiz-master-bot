question = [ {"question": "What is 2 + 2?", "answer": "4"},{"question": "Captial of Japan?", "answer": "Tokyo"},{"question": "How many days in a week?", "answer": "7"}]
for item in question:
    user_answer = input(item["question"] + " ")
    if user_answer == item["answer"]:
        print("Correct!")
    else:
        print("Wrong. The answer was", item["answer"])    