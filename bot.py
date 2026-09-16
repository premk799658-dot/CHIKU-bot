import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("TOKEN")
OWNER = "PREM BHUMIHAR"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = f"""
PREFIX-> / or .
OWNER-> {OWNER}
STATS-> ALIVE

Nc's
.fdnc -> PREM
.isaginc -> BHUMIHAR
.dnovnc -> KILLER
.flagnc -> 520
.hrtnc -> BHUMIHAR
.nonc -> PREM

SLIDER
.s | .slider
"""
    await update.message.reply_text(text)

async def slider(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = f"Slide by {OWNER} - SABKA BAAP HAI"
    if update.message.reply_to_message:
        name = update.message.reply_to_message.from_user.first_name
        await update.message.reply_text(f"{name} ko pel diya\n{msg}")
    else:
        await update.message.reply_text(msg)

async def all_nc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"NC DONE BY {OWNER}")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("slider", slider))
    app.add_handler(CommandHandler("s", slider))
    for c in ["fdnc","isaginc","dnovnc","flagnc","hrtnc","nonc"]:
        app.add_handler(CommandHandler(c, all_nc))
    app.run_polling()

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return f"{OWNER} BOT RUNNING"

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    flask_app.run(host='0.0.0.0', port=10000)
