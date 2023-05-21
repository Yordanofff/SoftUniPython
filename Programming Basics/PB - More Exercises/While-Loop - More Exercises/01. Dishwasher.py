consumption = {"dish": 5, "pot": 15}

bottles = int(input())
ml_of_detergent = bottles * 750

count = 0
num_plates = 0
num_pots = 0
detergent_used = 0
while True:
    count += 1
    num_to_be_washed = input()
    if num_to_be_washed == "End":
        break
    if count % 3 == 0:
        detergent_needed = int(num_to_be_washed) * consumption["pot"]
        num_pots += int(num_to_be_washed)
    else:
        detergent_needed = int(num_to_be_washed) * consumption["dish"]
        num_plates += int(num_to_be_washed)
    detergent_used += detergent_needed

    if detergent_used > ml_of_detergent:
        print(f"Not enough detergent, {detergent_used - ml_of_detergent} ml. more necessary!")
        break

if ml_of_detergent >= detergent_used:
    print("Detergent was enough!")
    print(f"{num_plates} dishes and {num_pots} pots were washed.")
    print(f"Leftover detergent {ml_of_detergent - detergent_used} ml.")
