import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config, load_config
from handlers import user_handlers, study_handlers
from keyboards.main_menu import set_main_menu





async def main():
    config: Config = await load_config()

    storage = MemoryStorage()
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(study_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())