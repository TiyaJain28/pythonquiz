import time
from questions import questions
from score import show_score

score = 0

time_limit = 120

print("===== PYTHON QUIZ =====")
print(f"You have {time_limit} seconds for each question.")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}. {q['question']}")

    for option in q['options']:
        print(option)

    start_time = time.time()

    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    end_time = time.time()

    total_time = end_time - start_time

    if total_time > time_limit:
        print("Time Up!")
    elif user_answer == q['answer']:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

show_score(score, len(questions))