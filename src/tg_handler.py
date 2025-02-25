import asyncio
from telegram import ForceReply, Update, Bot


async def msg(message: str) -> None:
    from .config import BOT_TOKEN, USER_ID
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=USER_ID, text=message)

# def main() -> None:
#     bot = Bot(token=BOT_TOKEN)
#     msg(bot)
#
#
#     """Start the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token(BOT_TOKEN).build()
#
#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#
#     # on non command i.e message - echo the message on Telegram
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#
#     # Run the bot until the user presses Ctrl-C
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
