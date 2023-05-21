name = input()

times_failed_to_pass_current_grade = 0
all_scores = []  # above 4
grade_count = 1

while grade_count <= 12:

    score = float(input())

    if score < 4:
        # Don't record to all_scores (failed to pass the grade - will repeat)
        times_failed_to_pass_current_grade += 1
        if times_failed_to_pass_current_grade == 2:
            print(f"{name} has been excluded at {grade_count} grade")
            break
    else:
        # got score above 4 - goes to the next grade
        grade_count += 1
        times_failed_to_pass_current_grade = 0
        all_scores.append(score)

if times_failed_to_pass_current_grade < 2:
    avg_score = sum(all_scores) / len(all_scores)
    print(f"{name} graduated. Average grade: {avg_score:.2f}")