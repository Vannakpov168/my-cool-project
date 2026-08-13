from telethon import TelegramClient, events

# ១. ជំនួស API ID និង API Hash ដែលទទួលបានពី my.telegram.org
API_ID = 1234567  # ដាក់លេខ API ID របស់អ្នកនៅទីនេះ (គ្មាន ' ')
API_HASH = 'your_api_hash_here'  # ដាក់ API Hash របស់អ្នកនៅទីនេះ

# ២. ដាក់ Username ឬ User ID របស់មនុស្សដែលផ្ញើសារមករំខានអ្នកនោះ
# ឧទាហរណ៍៖ 'username_person' (កុំដាក់សញ្ញា @)
TARGET_USER = 'target_username'

client = TelegramClient('userbot_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=TARGET_USER))
async def auto_reply(event):
    # សារដែលអ្នកចង់ឱ្យ Bot ឆ្លើយតបទៅគាត់
    reply_text = "សួស្តី! ខ្ញុំកំពុងរវល់ខ្លាំង មិនបានមើលសារទេ។ ប្រព័ន្ធនឹងឆ្លើយតបសារនេះដោយស្វ័យប្រវត្តិ។"
    
    # ឆ្លើយតបសារស្វ័យប្រវត្តិ
    await event.reply(reply_text)
    print(f"[Auto-Replied] បានឆ្លើយតបទៅកាន់ {TARGET_USER} រួចរាល់។")

print("Userbot កំពុងដំណើរការ...")
client.start()
client.run_until_disconnected()
