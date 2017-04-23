aliens = []

for alien_number in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:2]:
    print(alien);