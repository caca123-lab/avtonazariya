import os
import logging
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Environment variables
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEB_APP_URL = "https://abc123.serveo.net/webapp_home"  # Keyin o'zgartirasiz


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
👋 Salom {user.first_name}!

🚗 *AvtoNazariya* botiga xush kelibsiz!
Bu bot orqali haydovchilik guvohnomasi nazariyasiga tayyorlaning.

📊 *Imkoniyatlar:*
• 1132 ta rasmiy savollar
• Test rejimi (bepul)
• To'liq statistikalar
• Reyting tizimi

Quyidagi tugma orqali testni boshlang 👇
    """

    # WebApp tugmasi
    web_app_button = KeyboardButton("📱 Testni Boshlash", web_app=WebAppInfo(url=WEB_APP_URL))

    # Klaviatura
    keyboard = [[web_app_button]]
    [KeyboardButton("📊 Mening statistikam"), KeyboardButton("🏆 Reyting")],
    [KeyboardButton("ℹ️ Yordam"), KeyboardButton("💳 Obuna")]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 *Bot Buyruqlari:*

/start - Botni ishga tushirish
/help - Yordam
/test - Testni boshlash
/tariflar - Obuna tariflari

📞 *Admin:* @sizning_username
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def tariflar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tarif_text = """
💳 *Obuna Tariflari:*

🟢 7 kunlik - 30,000 so'm
• Cheksiz testlar
• Batafsil statistikalar
• Xatolar tahlili

🔵 30 kunlik - 60,000 so'm  
• 7 kunlik imkoniyatlar
• Shaxsiy maslahat
• Reytingda ishtirok

💸 To'lov: Click, Payme, Bank karta
    """
    await update.message.reply_text(tarif_text, parse_mode='Markdown')


async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Testni boshlash uchun 'Testni Boshlash' tugmasini bosing yoki WebApp ni oching!",
        parse_mode='Markdown'
    )


def main():
    try:
        # Botni yaratish
        application = Application.builder().token(BOT_TOKEN).build()

        # Command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("tariflar", tariflar))
        application.add_handler(CommandHandler("test", test_command))

        # Botni ishga tushirish
        logger.info("Bot ishga tushdi...")
        application.run_polling()

    except Exception as e:
        logger.error(f"Xatolik: {e}")


if __name__ == '__main__':
    main()