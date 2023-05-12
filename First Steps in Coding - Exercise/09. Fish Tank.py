length = int(input())
width = int(input())
height = int(input())
percent_other = float(input())/100

volume = length * width * height
other = volume * percent_other

volume_water_only = (volume - other)/1000
print(volume_water_only)
