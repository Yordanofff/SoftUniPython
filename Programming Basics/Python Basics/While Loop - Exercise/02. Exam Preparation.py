num_low_score_allowed = int(input())

total_score = 0
num_of_problems = 0
last_problem = ""
low_scores_left = num_low_score_allowed

task = input()
while task != "Enough":
    last_problem = task
    num_of_problems += 1
    score = int(input())
    total_score += score
    if score <= 4:
        low_scores_left -= 1
        if low_scores_left == 0:
            print(f"You need a break, {num_low_score_allowed} poor grades.")
            break
    task = input()

if low_scores_left > 0:
    avg_score = total_score / num_of_problems
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {num_of_problems}")
    print(f"Last problem: {last_problem}")
