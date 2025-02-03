import random
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from gradio_client import Client

# Telegram Bot Token
TOKEN = "7858692263:AAETS3a3ZtDygTvS3iWvlSeZyuXPZ8jnvks"

# Hidden server configuration
SERVERS = [
    "https://huggingface.co/spaces/BICORP/GOGOGOGO",
    "https://huggingface.co/spaces/BICORP/server-2",
    "https://huggingface.co/spaces/BICORP/server-3", 
    "https://huggingface.co/spaces/BICORP/server-4",
    "https://huggingface.co/spaces/BICORP/server-5",
    "https://huggingface.co/spaces/BICORP/server-6"
]

MODELS = [
    "Lake 1 Flash",
    "Lake 1 Base",
    "Lake 1 Advanced",
    "Lake 2 Chat [Closed Alpha]",
    "Lake 2 Base [Closed Beta]"
]

PRESETS = ["Fast", "Normal", "Quality", "Unreal Performance"]

def get_random_server():
    """Randomly select from available servers"""
    return random.choice(SERVERS)

def handle_chat(message: str, model: str, preset: str):
    """Process chat messages with automatic server selection"""
    try:
        client = Client(get_random_server())
        result = client.predict(
            message,
            model,
            preset,
            api_name="/chat"
        )
        return result
    except Exception as e:
        return "⚠️ Service unavailable. Please try your request again."

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your AI assistant. Send me a message and I'll reply.")

def chat(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    model = "Lake 1 Flash"  # Default model
    preset = "Normal"  # Default preset
    response = handle_chat(user_message, model, preset)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
