# Auto Telegram Name Change

Userbot для автоматической смены имени Telegram-аккаунта с помощью Telethon.

## Возможности
- Автоматически меняет имя (first_name) аккаунта по списку
- Работает как systemd-сервис
- Безопасно: ваши личные данные не публикуются
- Интервал смены имени — раз в 30 минут (можно изменить)

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/UrsickW/auto-telegram-name-change.git
   cd auto-telegram-name-change
   ```

2. **Создайте виртуальное окружение и установите зависимости:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install telethon
   ```

3. **Настройте файл `change_name.py`:**
   - Вставьте свой `api_id` и `api_hash` (получить на https://my.telegram.org)
   - При первом запуске потребуется ввести номер телефона и код из Telegram
   - Измените список имён по желанию

4. **Добавьте сервис (опционально):**
   - Отредактируйте путь к Python и рабочей директории в `change_name.service` при необходимости
   - Скопируйте сервис:
     ```bash
     sudo cp change_name.service /etc/systemd/system/
     sudo systemctl daemon-reload
     sudo systemctl enable --now change_name.service
     ```

## Пример запуска вручную
```bash
source venv/bin/activate
python3 change_name.py
```

## Важно
- Не публикуйте свои `api_id`, `api_hash` и session-файлы!
- Не запускайте userbot с разных серверов/IP — используйте один и тот же session-файл.
- Telegram ограничивает частоту смены имени (интервал 30 минут — безопасный).

## Лицензия
MIT 