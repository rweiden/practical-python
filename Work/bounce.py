# bounce.py
#
# Exercise 1.5
max_height = 100
new_height = max_height
velocity = 3 / 5
total_bounces = 1

while total_bounces < 11: 
    new_height = new_height * velocity
    print(f'{total_bounces} {round(new_height,4)}')
    total_bounces = total_bounces + 1
