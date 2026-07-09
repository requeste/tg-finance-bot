from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.enums import parse_mode

from handlers.expensive import load_data, save_data

rt = Router()

@rt.message(Command("start"))
async def start(message: types.Message):
    text =(
        "Привет! Я бот для отслеживания расходов. \n\n"
        "Чтобы записать расход, отправь сообщения в формате:"
        "<blockquote>сумма категория</blockquote> \n"
        "Команды: <blockquote>/stats - показать статистику\n/delete {категория} - удалить категорию\n/delete_all - удалить все категории</blockquote>"
    )
    await message.answer(text, parse_mode = parse_mode.ParseMode.HTML)

@rt.message(Command("stats"))
async def stats(message: types.Message):
    user_id = str(message.from_user.id)
    all = load_data()

    if user_id not in all or not all[user_id]:
        await message.answer("❌ Нет данных для отображения.")
        return
    
    user = all[user_id]

    stats = "\n".join([f"{category}: {amount}" for category, amount in user.items()])
    top = "\n".join([f"{category}: {amount}" for category, amount in sorted(user.items(), key = lambda x: x[1], reverse = True)[:3]])
    total = sum(user.values())
    doli = "\n".join([f"{category}: {round(amount / total * 100, 2)}%" for category, amount in sorted(user.items(), key = lambda x: x[1], reverse = True)])

    text = (
        f"📊 Статистика расходов: \n<blockquote>{stats}</blockquote>"
        f"\n\n🏆 Топ 3 категорий: \n<blockquote>{top}</blockquote>"
        f"\n\n📈 Доли категорий: \n<blockquote>{doli}</blockquote>"
    )

    await message.answer(text, parse_mode = parse_mode.ParseMode.HTML)

@rt.message(Command("delete"))
async def delete(message: types.Message):
    text = message.text.split()
    category = " ".join(text[1:]).capitalize()

    if not category:
        await message.answer("⚠️ Пожалуйста, укажите категорию для удаления.")
        return
    
    user_id = str(message.from_user.id)
    all = load_data()

    if user_id not in all or not all[user_id]:
        await message.answer("❌ Нет данных для удаления.")
        return
    
    user = all[user_id]
    
    if category not in user:
        await message.answer(f"❌ Категория '{category}' не найдена или уже удалена.")
        return

    del all[user_id][category]
    save_data(all)

    await message.answer(f"✅ Категория '{category}' успешно удалена.")

@rt.message(Command("delete_all"))
async def delete_all(message: types.Message):
    user_id = str(message.from_user.id)
    all = load_data()

    if user_id not in all or not all[user_id]:
        await message.answer("❌ Нет данных для удаления.")
        return
    
    del all[user_id]
    save_data(all)

    await message.answer("✅ Все данные успешно удалены.")

@rt.message()
async def echo(message: types.Message):
    text = message.text.strip()
    user_id = str(message.from_user.id)

    try:
        parts = text.split()
        if len(parts) < 2:
            await message.answer("⚠️ Напишите сумму и категорию через пробел.")
            return
        
        amount = float(parts[0])
        category = " ".join(parts[1:]).capitalize()

        all = load_data()

        if user_id not in all:
            all[user_id] = {}

        user = all[user_id]
        if category in user:
            user[category] += amount
        else:
            user[category] = amount

        save_data(all)

        await message.answer(f"✅ Записано: {amount} в категорию '{category}'.")
    
    except ValueError:
        await message.answer("❌ Ошибка в сумме. Пример: 100 продукты")