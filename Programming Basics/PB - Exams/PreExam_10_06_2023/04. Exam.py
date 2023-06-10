num_students = int(input())

total_score = 0
n1 = n2 = n3 = n4 = 0
for _ in range(num_students):
    score = float(input())
    total_score += score
    if score >= 5:
        n1 += 1
    elif score >= 4:
        n2 += 1
    elif score >= 3:
        n3 += 1
    else:
        n4 += 1

print(f"Top students: {n1 / num_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {n2 / num_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {n3 / num_students * 100:.2f}%")
print(f"Fail: {n4 / num_students * 100:.2f}%")
print(f"Average: {total_score / num_students:.2f}")
