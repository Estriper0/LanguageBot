from aiogram.types import BotCommand
from aiogram import Bot

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запуск бота'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
    ]

    await bot.set_my_commands(main_menu_commands)