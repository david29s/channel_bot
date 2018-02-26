import telebot

id='PLACE HOLDER FOR YOU TELEGRAM ID'
bot = telebot.TeleBot("PLACE HOLDER FOR YOUR TELEGRAM BOT API")


@bot.channel_post_handler(content_types=['audio', 'voice'])
def repeat_all_audios(audio):
    bot.forward_message(id, audio.chat.id, audio.message_id)

bot.polling(none_stop=True)