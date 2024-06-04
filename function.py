from aiogram.types import Message

async def startAnswer(message: Message):
    await message.answer("Assalomu Aleykum")
    
async def textAnswer(message: Message):
    await message.answer("Xabaringiz qabul qilindi !")