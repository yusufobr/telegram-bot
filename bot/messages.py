from telegram import Update
from telegram.ext import ContextTypes

# Response handler
def handle_response(text: str) -> str:
    if 'azul' in text.lower():
        return "Azul manik antegit ghassad 👋🏻👋🏻"
    return "I'm sorry, I only speak Amazigh language 😅"

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    BOT_USERNAME = context.bot.username  # Access bot's username from context
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User: {update.message.chat.id} | Message: {text} | Type: {message_type}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print(f"Bot: {response}")
    await update.message.reply_text(response)
