minutes_control = int(input())  # minutes
seconds_control = int(input())  # seconds

current_record_in_sec = minutes_control * 60 + seconds_control

track_len = float(input())  # meters
sec_for_100m = int(input())  # seconds

slowed_by_sec = track_len / 120 * 2.5  # sec

his_time_in_sec = track_len / 100 * sec_for_100m - slowed_by_sec

if his_time_in_sec <= current_record_in_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {his_time_in_sec:.3f}.")
else:
    print(f"No, Marin failed! He was {his_time_in_sec - current_record_in_sec:.3f} second slower.")
