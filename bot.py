import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🌸 CHIKU ji! ! /Prem h kya?")

async def kiss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("prem se apni gand mara le marnde ke baad tere aatma ko shanti milega 🤣🍌🫩!!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("kiss", kiss))

print("Bot Started")
app.run_polling()
