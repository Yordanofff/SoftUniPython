movie_name = input()
num_of_days = int(input())
num_of_tickets = int(input())
ticket_price = float(input())
percentage_for_the_cinema = int(input())
total_win = (num_of_days * num_of_tickets * ticket_price) * (100-percentage_for_the_cinema)/100
print(f"The profit from the movie {movie_name} is {total_win:.2f} lv.")