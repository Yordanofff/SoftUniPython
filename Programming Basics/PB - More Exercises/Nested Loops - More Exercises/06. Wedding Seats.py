letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

letter_end = input()
num_rows = int(input())
num_odd = int(input())

letter_end_index = letters.index(letter_end.lower()) + 1

counter = 0
for letter in letters[:letter_end_index]:
    for i in range(1, num_rows + 1):
        if i % 2 == 1:
            letters_to_use_at_the_end = num_odd
        else:
            letters_to_use_at_the_end = num_odd + 2
        for j in letters[:letters_to_use_at_the_end]:
            print(f"{letter.upper()}{i}{j}")
            counter += 1
    num_rows += 1
print(counter)
