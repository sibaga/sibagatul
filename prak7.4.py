'''
УВВ-111
Создайте функцию connect, которая позволяет фиктивно подключиться к WiFi. Для подключения необходимо знать SSID (название) и пароль от WiFi.
Пароль может быть пустым. Если передали пустой SSID, необходимо переключиться на использование мобильной сети (4G), вызвав другую функцию - switch_to_lte.
Обе функции не возвращают результата, но выводят сообщение в консоль.
'''


def switch_to_lte():
    print('Переключаемся на мобильную сеть')


def connect(SSID, password):
    if SSID == "":
        switch_to_lte()
    if password == "":
        print(f'Подключаемся к открытой "{SSID}"')
    else:
        print(f'Подключаемся к "{SSID}" используя пароль "{password}"')


connect('wifi-miit-open', '')
connect('Moscow WiFi Free', '')
connect('', '')
connect('DOM.RU', '12345678')
