fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

choice = input()
if choice in fruits:
    print("fruit")
elif choice in vegetables:
    print("vegetable")
else:
    print("unknown")