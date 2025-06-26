def ask_questions():
    questions = [
        "What is your name?",
        "How old are you?",
        "What is your favorite programming language?",
        "Where are you from?"
    ]
    answers = {}
    for question in questions:
        answer = input(question + " ")
        answers[question] = answer
    print("\nYour Answers:")
    for q, a in answers.items():
        print(f"{q} {a}")


if __name__ == "__main__":
    ask_questions()
