num_students = int(input())

list_all_scores = []
for i in range(num_students):
    score = float(input())
    list_all_scores.append(score)

r1 = [i for i in list_all_scores if 5 <= i]
r2 = [i for i in list_all_scores if 4 <= i < 5]
r3 = [i for i in list_all_scores if 3 <= i < 4]
r4 = [i for i in list_all_scores if 2 <= i < 3]  # fail

avg = sum(list_all_scores) / len(list_all_scores)

print(f"Top students: {len(r1) / len(list_all_scores) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {len(r2) / len(list_all_scores) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {len(r3) / len(list_all_scores) * 100:.2f}%")
print(f"Fail: {len(r4) / len(list_all_scores) * 100:.2f}%")
print(f"Average: {avg:.2f}")
