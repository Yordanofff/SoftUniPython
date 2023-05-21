n = int(input())

cmd = input()
list_all_scores = []
while not cmd == "Finish":
    current_sum = 0
    for i in range(n):
        score = float(input())
        current_sum += score
        list_all_scores.append(score)
    avg = current_sum / n
    print(f"{cmd} - {avg:.2f}.")

    cmd = input()

total_avg = sum(list_all_scores) / len(list_all_scores)
print(f"Student's final assessment is {total_avg:.2f}.")
