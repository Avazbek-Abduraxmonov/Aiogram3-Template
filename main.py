from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from asyncio import run
from function import *
from config import *

dp = Dispatcher()

async def run_bot(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishga tushdi")

async def down_bot(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishdan to'xtadi")
    
async def start():
    dp.startup.register(run_bot)
    dp.message.register(startAnswer, Command('start'))
    dp.message.register(textAnswer)
    dp.shutdown.register(down_bot)
    
    bot = Bot(token=token)
    await dp.start_polling(bot, polling_timeout=1)
    
run(start())