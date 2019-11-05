# Настройка бота
**Убедитесь что у вас установлен Python**

Откройте командную строку и напишите:
`python --version`
Должно получиться примерно так:
[![cmd-python-check](https://imgur.com/Gj8qr4z.png "cmd-python-check")](https://imgur.com/Gj8qr4z.png "cmd-python-check")

**Установка модулей в Python для работы бота**

Если python установлен, то в командную строку по очереди ( не обязательно в таком порядке же ) пропишите команды:
`pip install numpy`
`pip install pyautogui`
`pip install opencv-python==3.4.3.18`

**В коде настроить разрешение экрана**

[![screen-res-code](https://i.imgur.com/0A80Ecy.png "screen-res-code")](https://i.imgur.com/0A80Ecy.png "screen-res-code")

**Подогнать параметры так, чтобы скриншот делался по центру экрана**

[![screen-res-code-2](https://i.imgur.com/OHA1lot.png "screen-res-code-2")](https://i.imgur.com/OHA1lot.png "screen-res-code-2")

**Кнопка броска удочки**

В боте по умолчанию стоит кнопка броска W:   [![w-fishing](https://imgur.com/Rktk7JJ.png "w-fishing")](https://imgur.com/Rktk7JJ.png "w-fishing"). 

Если у вас другая - поменяйте ее в коде (на 19 и 35 строчке).

[![press_w_1](https://imgur.com/k1Ai4Sw.png "press_w_1")](https://imgur.com/k1Ai4Sw.png "press-w-1")

[![press-w-2](https://imgur.com/jmULnwa.png "press-w-2")](https://imgur.com/jmULnwa.png "press-w-2")

Вместо `pyautogui.press('w')` напишите, например, `pyautogui.press('2')`
# Запуск бота

**Сначала запустите игру любым удобным для вас способом**

[![game-start](https://imgur.com/7AGIq77.png "game-start")](https://imgur.com/7AGIq77.png "game-start")
бот работает как на российском (mail.ru) клиенте, так и на корейском

**Запустите консоль от *имени администратора(!!)**

[![cmd](https://imgur.com/wFqCdRb.png "cmd")](https://imgur.com/wFqCdRb.png "cmd")

**Пропишите через команду cd адрес, где находится файл main.py бота**

Если вы сохранили папку бота на диск C: то адрес  будет такой: 
`C:\AMD\lost-ark-fishing-bot`
В моем же случае:
[![cmd-cd](https://imgur.com/eEtsf8k.png "cmd-cd")](https://imgur.com/eEtsf8k.png "cmd-cd")

**Запуск бота**

В командной строке напишите команду:
`python main.py`
Если все сделали правильно, вы сразу заметите, что бот заработал:
[![cmd-bot-start](https://imgur.com/VkRpmdK.png "cmd-bot-start")](https://imgur.com/VkRpmdK.png "cmd-bot-start")

**Можно заходить в игру и рыбачить**

[![lost-ark-fishing-1](https://imgur.com/bq0zdb8.png "lost-ark-fishing-1")](https://imgur.com/bq0zdb8.png "lost-ark-fishing-1")