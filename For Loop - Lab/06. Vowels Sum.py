letters = ["a", "e", "i", "o", "u"]
text = input()
text_sum = 0
for i in text:
    if i in letters:
        index = letters.index(i)
        text_sum += index + 1

print(text_sum)
