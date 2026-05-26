from RagBot.app.quiz.quiz_generator import generate_quiz

def start_quiz(topic, difficulty):

    quizzes = generate_quiz(topic, difficulty)

    score = 0
    total_questions = len(quizzes)

    print(f"\n===== {topic.upper()} QUIZ =====")
    print(f"Difficulty Level: {difficulty}")

    for idx, quiz in enumerate(quizzes):

        print("\n--------------------------------")
        print(f"Question {idx + 1}")
        print("--------------------------------")

        print(quiz["question"])

        for i, option in enumerate(quiz["options"]):
            print(f"{i + 1}. {option}")

        try:
            choice = int(input("\nEnter your choice: "))
            selected_answer = quiz["options"][choice - 1]

        except:
            print("Invalid input.")
            continue

        if selected_answer.strip().lower() == quiz["answer"].strip().lower():

            print("\nCorrect ✅")
            score += 1

        else:

            print("\nWrong ❌")
            print(f"Correct Answer: {quiz['answer']}")

        print("\nExplanation:")
        print(quiz["explanation"])

    print("\n================================")
    print("QUIZ COMPLETED")
    print("================================")

    print(f"Final Score: {score}/{total_questions}")

    accuracy = score / total_questions

    return {
        "score": score,
        "total": total_questions,
        "accuracy": accuracy
    }