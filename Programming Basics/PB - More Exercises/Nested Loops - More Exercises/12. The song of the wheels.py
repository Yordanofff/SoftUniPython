m = int(input())

counter = 0
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == m:
                    if a < b and c > d:
                        counter += 1
                        if counter == 4:
                            password = f"{a}{b}{c}{d}"
                        print(f"{a}{b}{c}{d}", end=' ')

if counter > 0:
    print()

if password == "":
    print("No!")
else:
    print(f"Password: {password}")
