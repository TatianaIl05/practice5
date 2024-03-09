tower_1, tower_2, tower_3 = map(float, input('Введите высоты башен: ').split())
max_tower = tower_1
if tower_2 >= max_tower:
    max_tower = tower_2
if tower_3 >= max_tower:
    max_tower = tower_3
min_tower = tower_1
if tower_2 <= min_tower:
    min_tower = tower_2
if tower_3 <= min_tower:
    min_tower = tower_3
mid_tower = tower_1 + tower_2 + tower_3 - min_tower - max_tower
print(max_tower, mid_tower, min_tower)

# Another variant (without if)
min_tower = min(min(tower_1, tower_2), tower_3)
max_tower = max(max(tower_1, tower_2), tower_3)
mid = tower_1 + tower_2 + tower_3 - min_tower - max_tower
print(max_tower, mid_tower, min_tower)
