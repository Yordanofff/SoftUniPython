series_name = input()
season_count = int(input()) # 1..10
episode_count = int(input()) # 10..80
episode_len = float(input()) # 40.0..65.0

episode_len_with_ads = episode_len * 1.2
extra_time_for_all_seasons = season_count * 10  # minuti
total_time = int((season_count * episode_count * episode_len_with_ads) + extra_time_for_all_seasons)
print(f"Total time needed to watch the {series_name} series is {total_time} minutes.")
