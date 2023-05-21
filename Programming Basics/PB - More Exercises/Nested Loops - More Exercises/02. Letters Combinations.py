letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

letter_from = input()
letter_to = input()
letter_to_remove = input()

index_from = (letters.index(letter_from))
index_to = (letters.index(letter_to)) + 1

new_list = letters[index_from:index_to]

if letter_to_remove in new_list:
    index_to_remove = new_list.index(letter_to_remove)
    new_list.pop(index_to_remove)

combinations = []
for i in new_list:
    for j in new_list:
        for k in new_list:
            combinations.append(f"{i}{j}{k}")

print(f"{' '.join(combinations)} {len(combinations)}")
