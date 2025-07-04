from telethon import TelegramClient, functions, errors
import asyncio
import logging

api_id = 123456  # <-- Вставьте свой api_id
api_hash = 'your_api_hash'  # <-- Вставьте свой api_hash
session = 'my_userbot'  # session-файл, не удаляйте его после первого запуска!

names = [
    "𐌁𐌙 𐌵𐌐𐌔𐌉𐌂𐌊",
    "ꌃꌩ ꀎꋪꌗꀤꉓꀘ",
    "𝕭𝖞 𝖀𝖗𝖘𝖎𝖐",
    "ʙʏ ᴜʀsɪᴄᴋ",
    "𝐵𝓎 𝒰𝓇𝓈𝒾𝒸𝓀"
]

logging.basicConfig(filename='change_name.log', level=logging.INFO, format='%(asctime)s %(message)s')

INTERVAL = 30 * 60  # 30 минут в секундах

async def main():
    async with TelegramClient(
        session,
        api_id,
        api_hash,
        device_model="iPhone 55 Pro",
        system_version="iOS 100.1",
        app_version="Telegram 10.0",
        lang_code="en",
        system_lang_code="en"
    ) as client:
        i = 0
        while True:
            new_name = names[i % len(names)]
            try:
                await client(functions.account.UpdateProfileRequest(first_name=new_name))
                logging.info(f"Имя изменено на: {new_name}")
                i += 1
                await asyncio.sleep(INTERVAL)
            except errors.FloodWaitError as e:
                logging.warning(f"FloodWaitError: жду {e.seconds} секунд")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logging.error(f"Ошибка смены имени: {e}")
                await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main()) 