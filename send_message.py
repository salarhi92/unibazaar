from telethon import TelegramClient
from telethon.errors import FloodWaitError
import random
import asyncio
import os

api_id = 28003957
api_hash = '7f6d4eec65cbdbf02d201f7c39bf7ec9'
session_file = 'unibazaar_session.session'  # فایل سشن باید وجود داشته باشه

group_message_map = {
    "crypto_groups": {
        "groups": [
            "advertisement_N",
            "DoublyCommunityRU",
"DoublyCommunityBR",
"DoublyCommunityID",
"DoublyCommunityES",
"DoublyCommunityIR"
        ],
        "messages": [
            """⚡️🔥 The Key to True Magic is in Your Hands! 🔥⚡️

✨ Unlock abundance, love, and protection with our sacred stones and potent spells — all ritual-charged with your personal intention.
💎 Every product is carefully prepared to empower and elevate your life’s journey.

🌍 Worldwide secure shipping
🎁 Beautiful, gift-ready packaging

Take the first step now 👉 https://unibazaar.shop""",
            """💎✨  Spells & Stones — Perfect Energy Harmony ✨💎

🔮 Experience the Power of Ritual-Charged Crystals & Expertly Crafted Spells 🔮
Each item is cleansed, energized, and charged to support your highest goals and spiritual growth.
Witness transformative energy and manifest miracles in your daily life.

🌐 Shop easily at https://unibazaar.shop
📥 DM for custom requests or personalized magic kits""",
            """🌟🔮  Live the Magic with UniBazaar 🔮🌟

💫 From Ancient Wisdom to Modern Mysticism, All Made for You 💫
Empowering stones and tailored spells created with love and care to open the doors to success, love, and protection.
✨ Feel the real magic flow through your life — and watch your dreams manifest!

🛒 Order now at https://unibazaar.shop
📩 Message us for exclusive deals and personalized guidance!"""
        ]
    }
}

if not os.path.exists(session_file):
    print(f"[!] فایل سشن {session_file} پیدا نشد! باید قبلا ساخته باشی.")
    exit(1)

client = TelegramClient(session_file[:-8], api_id, api_hash)

async def send_messages():
    dialogs = await client.get_dialogs()
    for category in group_message_map.values():
        for dialog in dialogs:
            if dialog.is_group and dialog.entity.username in category['groups']:
                chosen_message = random.choice(category['messages'])
                try:
                    print(f"[+] ارسال پیام به گروه: {dialog.name}")
                    await client.send_message(dialog.id, chosen_message)
                    await asyncio.sleep(15)
                except FloodWaitError as e:
                    print(f"[!] محدودیت اسپم: صبر کن {e.seconds} ثانیه")
                    await asyncio.sleep(e.seconds + 15)
                except Exception as ex:
                    print(f"[!] خطا در ارسال پیام به {dialog.name}: {ex}")

async def main_loop():
    await client.connect()
    if not await client.is_user_authorized():
        print("[!] سشن معتبر نیست یا لاگین نشده.")
        return
    print("[*] اتصال موفق به تلگرام (با سشن ذخیره‌شده)")

    while True:
        await send_messages()
        print("[*] پیام‌ها ارسال شدند، 11.5 دقیقه صبر می‌کنم...")
        await asyncio.sleep(700)

if __name__ == '__main__':

    client.loop.run_until_complete(main_loop())

