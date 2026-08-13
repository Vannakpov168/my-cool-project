from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ជំនួស Bot Token ដែលបានមកពី BotFather នៅទីនេះ
BOT_TOKEN = "8047614722:AAHaV8uANS1U0QDRH0MWZmLTcQX327BZlEo"

# ដាក់ Telegram Username របស់មនុស្សដែលអ្នកចង់ reply (ឧទាហរណ៍: "john_doe")
# កុំដាក់សញ្ញា @
TARGET_USERNAME = "target_username"

async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.from_user:
        return

    # ឆែកមើលថា តើអ្នកដែលផ្ញើសារមកត្រូវជា TARGET_USERNAME ដែរឬទេ?
    sender_username = update.message.from_user.username
    
    if sender_username and sender_username.lower() == TARGET_USERNAME.lower():
        # សារដែលត្រូវ Auto Reply
        await update.message.reply_text("សួស្តី! ខ្ញុំកំពុងរវល់ មិនបានមើលសារទេ។")
        print(f"បាន Reply ទៅកាន់ @{sender_username} រួចរាល់។")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # ឱ្យ Bot ចាប់យកគ្រប់សារអត្ថបទ (Text)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_handler))
    
    print("Bot កំពុង ដំណើរការ (Running)...")
    app.run_polling()
