def show_score(score, total):
    print("\n===== QUIZ COMPLETED =====")
    print(f"Your Final Score: {score}/{total}")

    percentage = (score / total) * 100
    print(f"Percentage: {percentage}%")

    if score >= 8:
        print("Excellent!")
    elif score >= 5:
        print("Good Job!")
    else:
        print("Keep Practicing!")