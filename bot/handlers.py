from telegram import Update
from telegram.ext import ContextTypes

# Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Azul(Hello) 👋🏻👋🏻, thanks for chatting with me, I'm an Amazigh bot!")

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm an Amazigh bot, I can help you with some Amazigh words and phrases.")

# Custom Command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")
