# 5.5
# Сделайте список героев своей любимой игры (минимум 5).
# Каждый герой это массив из 3 элементов - Прозвище, Класс (мечник, лучник, маг), Сила
# Найдите самого сильного героя и самого слабого.
# Выведи их как показано в примере:
# Most Powerful: El Primo (Physical), has 188 Attack
# Least Powerful: Tick (Bomber), has 50 Attack
heroes = [["tracer", "dps", 150],
          ["Reinhardt", "tank", 600],
          ["Widowmaker", "dps", 300],
          ["zenyata", "support", 100],
          ["mercy", "support", 50]]

minn = 0
maxx = 10000

for i in range(0, 5):
    dgm = heroes[i][2]
    if maxx < dmg:
        maxx = dmg
        max_dps = i

    if minn > dgm:
        minn = dgm
        min_dps = i

print(f'Most Powerful: {heroes[max_dps][0]} ({heroes[max_dps][1]}), has {heroes[max_dps][2]} attack')
print(f'Least Powerful: {heroes[min_dps][0]} ({heroes[min_dps][1]}), has {heroes[min_dps][2]} attack')
