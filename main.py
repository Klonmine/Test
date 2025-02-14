import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7273306667:AAEHoDXQcL-qyVrYyLpywR55n2KuZso-M_A')

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Отправляем обратно тот же текст, который получили
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()