record_sec = float(input())
meters_to_cross = float(input())
time_for_1_meter = float(input())

delay = int(meters_to_cross/15) * 12.5

total_time_needed = (meters_to_cross * time_for_1_meter) + delay

if total_time_needed < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time_needed:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time_needed - record_sec):.2f} seconds slower.")