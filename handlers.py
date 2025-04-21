from aiogram import types
from aiogram.filters.command import Command
from aiogram import Router
from report import recount_format
from google_api import sheets
from json_utils import create_dump
from config import JSON_PATHS

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Используя этого бота, ты принимаешь полную ответственность на себя.\n"
        "Если отчёт не сходится — ты виноват.\n"
        "Таблица: http://bit.ly/4bJ4ggE\n"
        "По вопросам — @N0tly"
    )


@router.message(Command("recount"))
async def recount(message: types.Message):
    await message.reply("Составление займёт примерно 30 секунд. Бот не залагал, он считает.")
    save_state()
    await message.answer(recount_format())


def save_state():
    create_dump(JSON_PATHS["arcade"], sheets["arcade"].get_values("A2:B50"))

    for key in ["350", "1000", "1500", "2000"]:
        main_ranges = {"350": "A3", "1000": "C3:D50", "1500": "F3:G50", "2000": "I3:J50"}
        stock_ranges = main_ranges

        create_dump(JSON_PATHS["main"][key], sheets["main"].get_values(main_ranges[key]))
        create_dump(JSON_PATHS["stock"][key], sheets["stock"].get_values(stock_ranges[key]))

    create_dump(JSON_PATHS["defective"], sheets["defective"].get_values("A2:B5"))
    create_dump(JSON_PATHS["misc"], sheets["misc"].get_values("A2:B8"))
