import string

alphabet = list(string.ascii_letters)
list_to_ignore = ["n", "o", "c"]
word = ""
cmd = input()
while cmd != "End":
    if cmd in list_to_ignore:
        list_to_ignore.pop(list_to_ignore.index(cmd))
    else:
        if cmd in alphabet:
            word += cmd
    if len(list_to_ignore) == 0:
        print(word, end=" ")
        list_to_ignore = ["n", "o", "c"]
        word = ""
    cmd = input()
