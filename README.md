# 💖 Valentine Telegram Bot

An interactive Telegram bot built as a personal gift for a loved one. The bot sends random reasons why you love them and sweet compliments whenever they tap a button.

Feel free to use this project as a template if you want to create a similar surprise for your partner!

---

## ✨ Features

* **Privately Access-Controlled (Middleware)**: The bot only responds to you and your partner (based on Telegram user IDs). If anyone else tries to message the bot, it quietly ignores their requests.
* **Random Love Reasons**: Compliments and reasons are stored in a simple JSON file and delivered randomly.
* **Docker Ready**: Includes a `docker-compose.yml` with volume mounts for `config.env` and `reasons.json`, so you can update your messages on the fly without rebuilding the container.

---

## 📁 Project Structure

```text
.
├── app/
│   ├── handlers/
│   │   └── start_handlers.py # Handler for /start command and button clicks
│   └── middlewares.py        # Access control middleware (restricts to specified IDs)
├── config/
│   ├── config_reader.py      # Config parser powered by pydantic-settings
│   └── config.env            # Environment variables (bot token & user IDs - gitignored)
├── bot.py                    # Entry point & aiogram bot initialization
├── reasons.json              # List of love reasons & compliments
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/valentinka_bot.git
cd valentinka_bot
```

### 2. Configure environment variables

Create a `config/config.env` file with your credentials:

```env
BOT_TOKEN=your_telegram_bot_token
MY_ID=123456789
VARYA_ID=987654321
```

* `BOT_TOKEN` — Your bot token from [@BotFather](https://t.me/BotFather)
* `MY_ID` — Your Telegram User ID
* `VARYA_ID` — Your partner's Telegram User ID (you can find it via [@userinfobot](https://t.me/userinfobot))

### 3. Customize your reasons

Edit `reasons.json` with your own personal reasons and compliments:

```json
[
  "Your smile brightens up my whole day",
  "Even sitting in silence with you feels comforting",
  "I love how deeply you care about the things you do"
]
```

---

## 🛠 Running the Bot

### Option A: Using Docker Compose (Recommended)

```bash
docker compose up -d --build
```

### Option B: Local Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   # .venv\Scripts\activate  # On Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the bot:
   ```bash
   python bot.py
   ```
