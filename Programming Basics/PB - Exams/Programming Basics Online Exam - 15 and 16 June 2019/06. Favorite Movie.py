def calc_score(movie_title):
    movie_len = len(movie_title)
    sum = 0
    for i in movie_title:
        if i.islower():
            sum -= movie_len * 2
        elif i.isupper():
            sum -= movie_len

        sum += ord(i)
    return sum


i = 1
movie_dict_score = {}

while True:
    if i == 8:
        print("The limit is reached.")
        print(
            f"The best movie for you is {max(movie_dict_score, key=movie_dict_score.get)} with {max(movie_dict_score.values())} ASCII sum.")
        break

    cmd = input()

    if cmd == "STOP":
        print(
            f"The best movie for you is {max(movie_dict_score, key=movie_dict_score.get)} with {max(movie_dict_score.values())} ASCII sum.")
        break

    movie_dict_score[cmd] = calc_score(cmd)

    i += 1
