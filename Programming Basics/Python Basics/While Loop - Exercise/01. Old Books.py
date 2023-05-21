book_name = input()

book_search = ""
num_searched = 0
while book_search != book_name:
    book_search = input()
    if book_search == book_name:
        print(f"You checked {num_searched} books and found it.")

    if book_search == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {num_searched} books.")
        break
    num_searched += 1
