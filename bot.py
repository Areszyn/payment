import os
from flask import Flask, request
from pyrogram import Client

app = Flask(__name__)

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Your Vercel URL

bot = Client("star_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.route("/", methods=["GET"])
def home():
    return "⭐ Star Receiving Bot is Running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    update = request.get_json()
    bot.process_update(update)
    return "OK", 200

# Start the bot
if __name__ == "__main__":
    app.run(debug=True)
