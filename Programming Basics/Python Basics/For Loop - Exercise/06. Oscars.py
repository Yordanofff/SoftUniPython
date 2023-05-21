# done before... (just copied)
req_score = 1250.5
name = input()
academy_score = float(input())
num_judge = int(input())
total_judge_score = 0

for i in range(1, num_judge + 1):
    judge_name = input()
    judge_score = float(input())
    total_judge_score += (judge_score * len(judge_name)) / 2
    if req_score <= academy_score + total_judge_score:
        break

total_score = academy_score + total_judge_score

if total_score > req_score:
    print(f"Congratulations, {name} got a nominee for leading role with {total_score:.1f}!")
else:
    print(f"Sorry, {name} you need {(req_score - total_score):.1f} more!")
