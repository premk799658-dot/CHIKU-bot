import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8918005382:AAFW5TbaLSeGETCS5FU6psiTlazwwZ-j9Hc")
OWNER = "PREM BHUMIHAR"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = f"""
📌 PREFIX-> `/` or `.`
🎀 OWNER-> {PREM} ✓
🧿 STATS-> ALIVE

⊢≫Nc's
.fdnc → PREM
.isaginc → BHUMIHAR
.dnovnc → KILLER
.flagnc → 520
.hrtnc → BHUMIHAR
.nonc → PREM
.dicnc → PREM
.spdnc → BHUMIHAR
.exabotnc → KILLER
.mync → 520
.mxnc → PREM
.writnc → BHUMIHAR
.firenc → KILLER
.favshit → {OWNER}
.ultranc → PREM BAAP

⊢≫SLIDER
.s | .slider | .special | .anis | .swipe

⊢≫PHOTO
.savephoto | .PREMph
"""
    await update.message.reply_text

# (tatte Teri maa ki chut ki awaz kashmir tak pahucha dunga 🫩)
async def slider(update: Update, context: ContextTypes.DEFAULT_TYPE):
    OWNER = "PREM BHUMIHAR"  
    
    
    # ("tatte Teri maa ki chut ki awaz kashmir tak pahucha dunga 🫩){PREM} - SABKA BAAP HAI
    if update.message.reply_to_message:
        target_name = update.message.reply_to_message.from_user.first_name
        await update.message.reply_text(f"{PREM BAAP NE TUJHE To Pel Diya\)
    else:
        await update.message.reply_text(tatte Teri maa ki chut ki awaz kashmir tak pahucha dunga )

async def all_nc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"NC DONE BY {PREM} 👑")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler(/start .start)
    app.add_handler(CommandHandler(/help .start)
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("slider", slider))
    app.add_handler(CommandHandler("s", slider))
    app.add_handler(CommandHandler("special", slider))
    app.add_handler(CommandHandler("anis", slider))
    app.add_handler(CommandHandler("swipe", slider))
    for c in ["fdnc","isaginc","dnovnc","flagnc","hrtnc","nonc","dicnc","spdnc","exabotnc","mync","mxnc","writnc","firenc","favshit","ultranc","savephoto","isagiph"]:
        app.add_handler(CommandHandler(c, all_nc))
    app.run_polling()

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return f"{prem} BOT RUNNING"

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    flask_app.run(host='0.0.0.0', port=10000)
