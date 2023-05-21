period = int(input())
num_doctors = 7

treated_patients = 0
untreated_patients = 0

day_count = 1
for i in range(period):
    if day_count % 3 == 0 and untreated_patients > treated_patients:
        num_doctors += 1

    num_patients = int(input())
    
    if num_patients <= num_doctors:
        treated_patients += num_patients
    else:
        treated_patients += num_doctors
        untreated_patients += num_patients - num_doctors
    day_count += 1

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
