def is_distinct(year_to_check):
    year_full_len = len(str(year_to_check))
    len_all_non_repeatable_digits = len(set(tuple(int(j) for j in str(year_to_check))))
    return year_full_len == len_all_non_repeatable_digits


year = int(input())
year += 1
while not is_distinct(year):
    year += 1
print(year)