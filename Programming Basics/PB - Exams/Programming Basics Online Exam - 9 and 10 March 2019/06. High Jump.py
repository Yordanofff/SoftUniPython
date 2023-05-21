height_wanted = int(input())  # cm

current_height = height_wanted - 30

won = failed = False
total_tries = 0
counter = 0
while True:
    for _ in range(3):
        counter += 1
        total_tries += 1
        current_jump = int(input())

        if current_jump > current_height:
            if current_height >= height_wanted and current_jump > height_wanted:
                won = True
                break
            current_height += 5
            counter = 0
        else:
            if counter == 3:
                failed = True
                break
    if failed or won:
        break

if failed:
    print(f"Tihomir failed at {current_height}cm after {total_tries} jumps.")
elif won:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_tries} jumps.")
