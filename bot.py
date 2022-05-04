from parser import Anecdote
import telebot


class MyBot:
    token = '5127621218:AAGmRY1kZqdEavldoHDjjRB99XO9fLjK0Xw'
    button_dict = dict()
    anecdote = Anecdote()

    def __init__(self, token='5127621218:AAGmRY1kZqdEavldoHDjjRB99XO9fLjK0Xw'):
        self.token = token
        self.button_dict = self.anecdote.make_buttons()

    def start_bot(self):
        bot = telebot.TeleBot(self.token)

        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, "Привет, я бот-анекдот, помогу найти прикол на любую тему. "
                                              "Напиши /topics, чтобы увидеть темы анекдотов.")

        def make_buttons():
            markup = telebot.types.InlineKeyboardMarkup()
            for topic in self.button_dict.keys():
                markup.add(telebot.types.InlineKeyboardButton(text=topic,
                           callback_data=topic))
            return markup

        @bot.message_handler(commands=['topics'])
        def handle_command(message):

            bot.send_message(chat_id=message.chat.id,
                             text='Вот темы анекдотов. Выбирайте',
                             reply_markup=make_buttons(),
                             parse_mode='HTML')

        @bot.callback_query_handler(func=lambda a: True)
        def react_on_buttons(call):
            bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=True,
                                      text=self.anecdote.make_anecdote(self.button_dict[call.data]))

        bot.polling(non_stop=True, interval=0)
