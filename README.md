Чтобы запустить бота (гайд для нубов):
> 1. Убедитесь, что установлен _Python **3.11**_ (Скачать можно [**Тут**](https://www.python.org/downloads/))
> 2. Скопируйте код на свое устройства `git clone https://github.com/dogekiller21/SneakerBox_Nikitoska_tg_bot`
> 3. Получите токен для бота у [**BotFather**](https://t.me/BotFather)
> 4. Создаем новое приложение в Reddit по [**ссылочке**](https://www.reddit.com/prefs/apps)
> 5. Переименуйте файлик `.env.example` в `.env` и вставьте в него **токен из BotFather** и **данные от Reddit приложения**
> 6. Создайте venv для проекта `python -m venv venv`
> 7. Активируйте venv (`venv/Scripts/activate.bat` для Windows, `source venv/bin/activate` для Linux)
> 8. Установите все нужные либы `pip install -r requirements.txt`
> 9. Запускайте файлик `main.py`

Шот бы юзать:
> 1. Команда `/re_evaluation` - парсит **\[UPC-EAN]**
> 2. Команда `/stock` - парсит **\[UPC-EAN]** и **\[C128]** \
> _После эти команд пишем боту *то, что он попросит*, в том формате, в котором он попросит_
> 3. Команды `/random_cat` и `/random_meme` - берет с Reddit рандомные пикчи котиков и мемы (`/r/cats` и `/r/memes`)
