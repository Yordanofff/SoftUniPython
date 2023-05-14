def school_camp_app(season, sex, num_students, days_stay):
    separated_prices = {"Winter": 9.6, "Spring": 7.2, "Summer": 15}
    mixed_prices = {"Winter": 10, "Spring": 9.5, "Summer": 20}

    girls_sport = {"Winter": "Gymnastics", "Spring": "Athletics", "Summer": "Volleyball"}
    boys_sport = {"Winter": "Judo", "Spring": "Tennis", "Summer": "Football"}
    mixed_sport = {"Winter": "Ski", "Spring": "Cycling", "Summer": "Swimming"}

    if num_students < 10:
        discount = 0
    elif num_students <= 19:
        discount = 0.05
    elif num_students <= 50:
        discount = 0.15
    else:
        discount = 0.5

    sport_dict_to_use = mixed_sport
    prices_dict_to_use = mixed_prices
    if sex == "girls":
        sport_dict_to_use = girls_sport
        prices_dict_to_use = separated_prices
    elif sex == "boys":
        sport_dict_to_use = boys_sport
        prices_dict_to_use = separated_prices

    price = prices_dict_to_use[season] * num_students * days_stay * (1 - discount)
    sport = sport_dict_to_use[season]
    print(f"{sport} {price:.2f} lv.")


# season = input()
# sex = input()
# students = int(input())
# days = int(input())
#
# school_camp_app(season, sex, students, days)

school_camp_app("Spring", "girls", 20, 7)
school_camp_app("Spring", "mixed", 17, 14)
school_camp_app("Summer", "boys", 60, 7)
school_camp_app("Winter", "mixed", 9, 15)

# todo - 1 case not working...