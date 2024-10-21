import re
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

# Response handler
def handle_response(text: str) -> str:
    # Normalize the text to lower case
    text = text.lower()
    
    # Case 1: Azul Greeting
    if 'azul' in text:
        return "Azul manik antegit ghassad 👋🏻👋🏻"
    
    # Case 2: User says "thanks" or "thank you"
    elif 'thanks' in text or 'thank you' in text:
        return "You're welcome! 👋🏻"
    
    # Case 3: User asks for time
    elif 'time' in text:
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}"
    
    # Case 4: User says "Good morning"
    elif 'good morning' in text:
        return "Good morning! Have a wonderful day!"
    
    # Case 5: Greeting in other languages
    elif any(greet in text for greet in ['hola', 'salut', 'ciao', 'مرحبا']):
        return "Hello! But I only speak Amazigh language for now 😅"
    
    # Case 6: User asks for the bot’s name
    elif 'what is your name' in text:
        return "I am an Amazigh bot, here to help you learn some Amazigh words and phrases."
    
    # Case 7: User asks for a joke
    elif 'joke' in text:
        return "Why don't skeletons fight each other? Because they don't have the guts! 😄"
    
    # Case 8: User says "Teach me Amazigh"
    elif 'teach me amazigh' in text:
        return "Sure! Here's a word: 'azul' means 'hello'. 👋🏻"
    
    # Case 9: Handle common typos for "Azul"
    elif re.search(r'\bazlu\b', text):
        return "Did you mean 'Azul'? It means 'Hello' in Amazigh! 👋🏻"
    
    # Default response
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
