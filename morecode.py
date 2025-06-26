import os
import json


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

    # Additional functionality: Save answers to a file and allow reviewing previous answers

    def save_answers(answers, filename="answers.json"):
        with open(filename, "w") as f:
            json.dump(answers, f, indent=4)
        print(f"\nAnswers saved to {filename}")

    def load_answers(filename="answers.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
        else:
            print("No previous answers found.")
            return None

    def main():
        print("Welcome to the interactive questionnaire!")
        while True:
            print("\nMenu:")
            print("1. Answer questions")
            print("2. Review previous answers")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")
            if choice == "1":
                answers = {}
                questions = [
                    "What is your name?",
                    "How old are you?",
                    "What is your favorite programming language?",
                    "Where are you from?"
                ]
                for question in questions:
                    answer = input(question + " ")
                    answers[question] = answer
                print("\nYour Answers:")
                for q, a in answers.items():
                    print(f"{q} {a}")
                save_answers(answers)
            elif choice == "2":
                previous = load_answers()
                if previous:
                    print("\nPrevious Answers:")
                    for q, a in previous.items():
                        print(f"{q} {a}")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    if __name__ == "__main__":
        main()

# saddasdas
