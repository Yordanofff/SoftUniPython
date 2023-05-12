num = float(input())
if 0 < num < 1:
    print("small positive")
elif 1 < num < 1_000_000:
    print("positive")
elif num > 1_000_000:
    print("large positive")
elif -1 < num < 0:
    print("small negative")
elif -1_000_000 < num < -1:
    print("negative")
elif num < -1_000_000:
    print("large negative")
else:
    print("zero")