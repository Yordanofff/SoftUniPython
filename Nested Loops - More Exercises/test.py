letters = ["нула", "едно", "две", "три", "четири", "пет", "шест", "седем", "осем", "девет", "десет", "единадесет",
           "дванадесет"]

alfabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х",
           "ц", "ч", "ш", "щ", "ь", "ю", "я"]

repeated = ["десет", ] + letters[1:10]
# print(repeated)

def convert_num_to_text(i):
    if i <= 12:
        return letters[i]
    elif i <= 19:
        return f"{repeated[i % 10]}надесет"
    elif i == 20:
        return "двадесет"
    elif i < 30:
        return f"двадесет и {repeated[i % 10]}"
    elif i < 100:
        if i % 10 == 0:
            return f"{repeated[i // 10]}десет"
        else:
            return f"{repeated[i // 10]}десет и {repeated[i % 10]}"
    elif i == 100:
        return "сто"
    elif i < 1000:
        if i // 100 <= 3:
            h_start_with = "ста"
        else:
            h_start_with = " стотин"
        if i % 100 == 0:
            return f"{repeated[i//100]}{h_start_with}"
        elif i % 100 <= 20:
            return f"{repeated[i//100]}{h_start_with} и {convert_num_to_text(i % 100)}"
        else:
            return f"{repeated[i//100]}{h_start_with} {convert_num_to_text(i % 100)}"
    elif i == 1000:
        return "хиляда"
    elif i < 10_000:
        if i // 1000 == 1:
            start_with = "хиляда"
        else:
            start_with = f"{repeated[i//1000]} хиляди"

        if i % 1000 == 0:
            return start_with
        elif i % 100 <= 20 and i // 100 == 10:
            # 1000-1020
            return f"{start_with} и {convert_num_to_text(i % 1000)}"
        else:
            return f"{start_with} {convert_num_to_text(i % 1000)}"
    elif i == 10_000:
        return f"{repeated[0]} хиляди"



def get_names_up_to_99():
    list_all_words = []
    for i in range(100):
        list_all_words.append(convert_num_to_text(i))
        # if i <= 12:
        #     list_all_words.append(letters[i])
        # elif i <= 19:
        #     list_all_words.append(f"{repeated[i % 10]}надесет")
        # elif i == 20:
        #     list_all_words.append("двадесет")
        # elif i < 30:
        #     list_all_words.append(f"двадесет и {repeated[i % 10]}")
        # elif i < 100:
        #     if i % 10 == 0:
        #         list_all_words.append(f"{repeated[i // 10]}десет")
        #     else:
        #         list_all_words.append(f"{repeated[i // 10]}десет и {repeated[i % 10]}")
    return list_all_words

# print(get_names_up_to_99())
list_all_words = []
for i in range(10000):
    x = convert_num_to_text(i)
    list_all_words.append(x)


is_printed = False
for i in alfabet:
    for word in list_all_words:
        if i in word:
            print(f"{i} - {word}")
            is_printed = True
            break
    if not is_printed:
        print(f"{i} - ")
    else:
        is_printed = False
