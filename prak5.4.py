# 5.4
# Сделайте плейлист из нескольких треков (минимум 5).
# Каждый трек представляет из себя массив из 3 элементов - Исполнитель, Название, Альбом
# Выведите случайный трек из вашего плейлист
# Пример:
# Rick Astley - Never Gonna Give You Up (Album: Whenever You Need Somebody)
import random

playlist = [["Metallica", "Blackened", "…And Justice for All"],
            ["Metallica", "…And Justice for All", "…And Justice for All"],
            ["Metallica", "Eye of the Beholder", "…And Justice for All"],
            ["Metallica", "One", "…And Justice for All"],
            ["Metallica", "The Shortest Straw", "…And Justice for All"]]

i = random.randint(0, 4)

print(f'{playlist[i][0]} - {playlist[i][1]} (Album: {playlist[i][2]})')