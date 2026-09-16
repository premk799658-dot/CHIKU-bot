import os
import threading
import logging

from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ==================================================
# CONFIG
# ==================================================

TOKEN = os.getenv("TOKEN")
OWNER = "PREM BHUMIHAR"

if not TOKEN:
    raise RuntimeError(
        "TOKEN environment variable is missing. "
        "Set TOKEN in your hosting environment."
    )

# ==================================================
# LOGGING
# ==================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ==================================================
# MENU TEXT
# ==================================================

MENU_TEXT = """
╔══════════════════════════════╗
        🖤  CHIKU BOT  🖤
╚══════════════════════════════╝

📌 PREFIX → /  or  .

👑 OWNER → PREM BHUMIHAR
💠 STATUS → ALIVE ✓

━━━━━━━━━━━━━━━━━━━━━━

╭──「 NC'S 」
│
│ .menu → MENU
│ .alive → PREM ALIVE
│ .ping → PONG
│ .about → ABOUT BOT
│ .owner → PREM BHUMIHAR
│
╰──────────────────────

━━━━━━━━━━━━━━━━━━━━━━

╭──「 SLIDER 」
│
│ .special → PREM SPECIAL
│ .anis → PREM ANIS
│ .swipe → PREM SWIPE
│
╰──────────────────────

━━━━━━━━━━━━━━━━━━━━━━

╭──「 FUN 」
│
│ .dice → ROLL DICE
│ .coin → COIN FLIP
│ .rps → ROCK PAPER SCISSORS
│
╰──────────────────────

━━━━━━━━━━━━━━━━━━━━━━

╭──「 CONTROL 」
│
│ /start → START BOT
│ /menu → SHOW MENU
│ /help → HELP
│
╰──────────────────────

━━━━━━━━━━━━━━━━━━━━━━

🔥 PREM KILLER BOT
💎 PREM KING
🖤 BHUMIHAR POWER
"""

# ==================================================
# BASIC COMMANDS
# ==================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖤 PREM KILLER BOT RUNNING ✓\n\n"
        "Type /menu to see all commands."
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU_TEXT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖤 PREM BOT HELP\n\n"
        "/start - Start bot\n"
        "/menu - Show menu\n"
        "/alive - Check status\n"
        "/ping - Check response\n"
        "/about - About bot\n"
        "/owner - Owner info\n"
        "/dice - Roll dice\n"
        "/coin - Flip coin"
    )


async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 PREM BOT IS ALIVE ✓\n"
        "👑 OWNER → PREM BHUMIHAR"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 PONG ✓")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖤 CHIKU BOT\n\n"
        "👑 OWNER → PREM BHUMIHAR\n"
        "💠 STATUS → ALIVE ✓\n"
        "🔥 POWERED BY PREM KING"
    )


async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 BOT OWNER\n\n"
        "PREM BHUMIHAR 🖤"
    )


# ==================================================
# FUN COMMANDS
# ==================================================

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    number = random.randint(1, 6)
    await update.message.reply_text(
        f"🎲 PREM DICE\n\nResult → {number}"
    )


async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    result = random.choice(["HEADS", "TAILS"])
    await update.message.reply_text(
        f"🪙 PREM COIN\n\nResult → {result}"
    )


async def rps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✊ ROCK\n"
        "✋ PAPER\n"
        "✌️ SCISSORS\n\n"
        "Use your favourite game logic here."
    )


# ==================================================
# DOT COMMANDS
# ==================================================

async def dot_commands(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip().lower()

    commands = {
        ".menu": MENU_TEXT,
        ".alive": "🟢 PREM BOT IS ALIVE ✓",
        ".ping": "🏓 PONG ✓",
        ".about": (
            "🖤 CHIKU BOT\n"
            "👑 OWNER → PREM BHUMIHAR"
        ),
        ".owner": "👑 OWNER → PREM BHUMIHAR",
        ".special": "✨ PREM SPECIAL 🖤",
        ".anis": "🖤 PREM ANIS",
        ".swipe": "🔥 PREM SWIPE",
    }

    if text in commands:
        await update.message.reply_text(commands[text])


# ==================================================
# FLASK SERVER
# ==================================================

flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "PREM KILLER BOT RUNNING ✓"


@flask_app.route("/health")
def health():
    return "OK"


def run_flask():
    port = int(os.environ.get("PORT", 10000))

    flask_app.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False,
    )


# ==================================================
# MAIN
# ==================================================

def main():
    app = Application.builder().token(TOKEN).build()

    # Slash commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("alive", alive))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("owner", owner))
    app.add_handler(CommandHandler("dice", dice))
    app.add_handler(CommandHandler("coin", coin))
    app.add_handler(CommandHandler("rps", rps))

    # Dot commands
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            dot_commands
        )
    )

    print("====================================")
    print("🖤 PREM KILLER BOT STARTING...")
    print("👑 OWNER: PREM BHUMIHAR")
    print("💎 CREDIT: PREM KING")
    print("🟢 STATUS: ALIVE")
    print("====================================")

    app.run_polling()


# ==================================================
# START BOTH SERVERS
# ==================================================

if __name__ == "__main__":
    threading.Thread(
        target=run_flask,
        daemon=True
    ).start()

    main()
