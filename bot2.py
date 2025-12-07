import telebot
    
    # Инициализация бота с использованием его токена
bot = telebot.TeleBot("8208366636:AAHB34JMkUmdPJUS7n0RCz3vM-5ycaAumzs")
    
    # Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=["poll"])
def create_poll(message):
    answer_options = ["мемеме", "бубубу", "мимими", "блеблебле"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="бебебе",
        options=answer_options,
        type="quiz",
        correct_option_id=0,
        is_anonymous=False,
    )


@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass


# Запуск бота
bot.polling()