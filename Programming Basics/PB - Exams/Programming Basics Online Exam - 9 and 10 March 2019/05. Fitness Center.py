num_visitors = int(input())

options = {"Back": 0, "Chest": 0, "Legs": 0, "Abs": 0, "Protein shake": 0, "Protein bar": 0}

for _ in range(num_visitors):
    cmd = input().strip()
    options[cmd] += 1

sum_all = sum(list(options.values()))

sum_protein = sum(list(options.values())[-2:])

print(f"{options['Back']} - back")
print(f"{options['Chest']} - chest")
print(f"{options['Legs']} - legs")
print(f"{options['Abs']} - abs")
print(f"{options['Protein shake']} - protein shake")
print(f"{options['Protein bar']} - protein bar")
print(f"{(sum_all - sum_protein) / sum_all * 100:.2f}% - work out")
print(f"{sum_protein / sum_all * 100:.2f}% - protein")
