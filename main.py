from dotenv import load_dotenv
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Import handlers and logic from other files
from bot.handlers import start_command, help_command, custom_command
from bot.messages import handle_message
from bot.errors import error

load_dotenv()

TOKEN = os.getenv("TOKEN")

if __name__ == "__main__":
    print("Bot is running...")

    # Initialize the bot application
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling the bot
    print("Bot is polling ...")
    app.run_polling(poll_interval=3)
