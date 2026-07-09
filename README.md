# 📊 TG Expense Tracker [RU]

Асинхронный Telegram-бот для удобного учета и аналитики личных расходов по категориям. 

## ✨ Особенности (Features)
* 💰 **Быстрая запись:** ввод расходов в одно сообщение в формате `сумма категория`.
* 📈 **Умная статистика:** вывод общих трат, топа категорий и автоматический расчет процентной доли каждой категории от общего бюджета.
* ❌ **Управление данными:** возможность быстрого удаления ошибочно введенной категории с помощью команды `/delete <категория>`.
* 🔒 **Безопасность:** многопользовательский режим (каждый пользователь видит только свои расходы) и изоляция токенов через переменные окружения.

## 🛠 Стек технологий (Tech Stack)
* **Язык:** Python 3.11+
* **Фреймворк:** aiogram 3.x (Asyncio)
* **Хранилище данных:** JSON-файлы (встроенные словари Python)
* **Конфигурация:** python-dotenv

## 🚀 Как запустить проект локально

### 1. Клонируйте репозиторий:
```bash
git clone [https://github.com/requeste/tg-finance-bot.git](https://github.com/твой_юзернейм/tg-finance-bot.git)
cd tg-finance-bot
```
### 2. Настройте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Установите зависимости:
```bash
pip install aiogram python-dotenv
```
### 4. Создайте файл конфигурации:
Создайте в корне проекта файл .env и добавьте туда ваш токен от BotFather:
```Plaintext
BOT_TOKEN=...
```
### 5. Запустите бота:
```bash
python bot.py
```
## 📝 Планы по развитию (Roadmap)
* [ ] Перенос хранилища с JSON на базу данных SQLite.
* [ ] Интеграция Inline-кнопок для более удобного UI/UX.
* [ ] Фильтрация статистики по временным периодам (день, неделя, месяц).
# 📊 TG Expense Tracker [ENG]

An asynchronous Telegram bot for convenient tracking and analysis of personal expenses by category. 

## ✨ Features
* 💰 **Quick Entry:** Enter expenses in a single message using the format `amount category`.
* 📈 **Smart Statistics:** displays total spending, top categories, and automatically calculates each category’s percentage of the total budget.
* ❌ **Data Management:** quickly delete a category entered by mistake using the command `/delete <category>`.
* 🔒 **Security:** multi-user mode (each user sees only their own expenses) and token isolation via environment variables.

## 🛠 Tech Stack
* **Language:** Python 3.11+
* **Framework:** aiogram 3.x (Asyncio)
* **Data Storage:** JSON files (built-in Python dictionaries)
* **Configuration:** python-dotenv

## 🚀 How to Run the Project Locally

### 1. Clone the repository:
```bash
git clone [https://github.com/requeste/tg-finance-bot.git](https://github.com/твой_юзернейм/tg-finance-bot.git)
cd tg-finance-bot
```
### 2. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies:
```bash
pip install aiogram python-dotenv
```
### 4. Create a configuration file:
Create a .env file in the project root and add your token from BotFather to it:
```Plaintext
BOT_TOKEN=...
```
### 5. Run the bot:
```bash
python bot.py
```
# 📝 Development Plans (Roadmap)
* [ ] Migrate storage from JSON to an SQLite database.
* [ ] Integrate inline buttons for a more user-friendly UI/UX.
* [ ] Filter statistics by time periods (day, week, month).