movie = input()

num_students_all = num_kids_all = num_standard_all = 0

while not movie == "Finish":
    total_seats = int(input())
    num_students = num_kids = num_standard = 0

    cmd = input()
    n = 0
    while not cmd == "End":
        if cmd == "standard":
            num_standard += 1
        elif cmd == "student":
            num_students += 1
        elif cmd == "kid":
            num_kids += 1

        n += 1

        if n == total_seats:
            break

        cmd = input()

    num_standard_all += num_standard
    num_kids_all += num_kids
    num_students_all += num_students

    total_num = num_kids + num_students + num_standard
    percentage = total_num / total_seats * 100
    print(f"{movie} - {percentage:.2f}% full.")
    movie = input()  # new movie

total_num_all = num_students_all + num_standard_all + num_kids_all
p_students = num_students_all / total_num_all * 100
p_standard = num_standard_all / total_num_all * 100
p_kids = num_kids_all / total_num_all * 100

print(f"Total tickets: {total_num_all}")
print(f"{p_students:.2f}% student tickets.")
print(f"{p_standard:.2f}% standard tickets.")
print(f"{p_kids:.2f}% kids tickets.")
