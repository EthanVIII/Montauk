from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
USER_ID = os.getenv("TELEGRAM_TARGET_ID")
