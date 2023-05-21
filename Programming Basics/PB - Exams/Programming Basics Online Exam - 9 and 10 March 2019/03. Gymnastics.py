ribbon_view = {"Russia": 9.1, "Bulgaria": 9.6, "Italy": 9.2}
ribbon_diff = {"Russia": 9.4, "Bulgaria": 9.4, "Italy": 9.5}

hoop_view = {"Russia": 9.3, "Bulgaria": 9.55, "Italy": 9.45}
hoop_diff = {"Russia": 9.8, "Bulgaria": 9.75, "Italy": 9.35}

rope_view = {"Russia": 9.6, "Bulgaria": 9.5, "Italy": 9.7}
rope_diff = {"Russia": 9, "Bulgaria": 9.4, "Italy": 9.15}

country = input()
type = input()

total_score = 0
if type == "ribbon":
    total_score = ribbon_diff[country] + ribbon_view[country]
elif type == "hoop":
    total_score = hoop_diff[country] + hoop_view[country]
elif type == "rope":
    total_score = rope_diff[country] + rope_view[country]

percent_to_max = (20 - total_score) / 20 * 100

print(f"The team of {country} get {total_score:.3f} on {type}.")
print(f"{percent_to_max:.2f}%")
