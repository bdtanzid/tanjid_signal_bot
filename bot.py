import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Signal Bot Ready!")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(["📈 UP", "📉 DOWN"])
    await update.message.reply_text(result)

app = Application.builder().token("YOUR_BOT_TOKEN").build(8506912991:AAHPNw96iqvzjq9JhPKbvvFmlHq7-c6VZEY)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()
