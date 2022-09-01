player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
    'fav_food': ["pizza", "hamburger"]
}

print(player.get('name'))
print(player.pop('age'))
player['xp'] = 1500
print(player)
player.get("fav_food").append("rice")
print(player)