import datetime

import config
from json_utils import json_sum_of_all, json_to_str, json_for_one_item
from config import JSON_PATHS


def section(title, path):
    return f"\n\n{title}:\nОбщее количество - {json_sum_of_all(path)}\n\n{json_to_str(path)}"


def recount_format():
    now = datetime.datetime.now()
    date_str = now.strftime("%d.%m.%y")
    time_label = "Утренний пересчёт" if now.hour < 16 else "Вечерний пересчёт"

    result = [
        time_label,
        date_str,
        f"{config.SHOP_NAME}\n\nТир витрина:",
        f"Призовая - {json_for_one_item(JSON_PATHS['main']['350'])}",
        section("Охотник", JSON_PATHS['main']['1000']),
        section("Снайпер", JSON_PATHS['main']['1500']),
        section("Пехотинец", JSON_PATHS['main']['2000']),
        f"\n\n\nАркада витрина - {json_sum_of_all(JSON_PATHS['arcade'])}",
        f"\n\n{json_to_str(JSON_PATHS['arcade'])}",
        "\n\n\nЗапас:\n",
        f"\nПризовые - {json_for_one_item(JSON_PATHS['stock']['350'])}",
        section("Охотник", JSON_PATHS['stock']['1000']),
        section("Снайпер", JSON_PATHS['stock']['1500']),
        section("Пехотинец", JSON_PATHS['stock']['2000']),
        "\n\n\nБрак:\n",
        json_to_str(JSON_PATHS['defective']),
        "\n\n*Прочее*\n",
        json_to_str(JSON_PATHS['misc'])
    ]

    return "\n".join(result)
