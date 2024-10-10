from telegram import Update
from telegram.ext import ContextTypes

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"An error occurred caused by {update}: {context.error}")
