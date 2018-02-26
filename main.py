import telebot

<<<<<<< HEAD
id='PLACE HOLDER FOR YOU TELEGRAM ID'
bot = telebot.TeleBot("PLACE HOLDER FOR YOUR TELEGRAM BOT API")
=======
bot = telebot.TeleBot("PLACE HOLDER FOR YOUR TELEGRAM BOT API")

admin_id='PLACE HOLDER FOR YOU TELEGRAM ID'
>>>>>>> c747bdf55fee9027f4c90099f59e109503401f2b

@bot.channel_post_handler(content_types=['audio', 'voice'])
def repeat_all_audios(audio):
    print(audio)
<<<<<<< HEAD
    bot.forward_message(id, audio.chat.id, audio.message_id)
=======
    bot.forward_message(admin_id, audio.chat.id, audio.message_id)
>>>>>>> c747bdf55fee9027f4c90099f59e109503401f2b

bot.polling(none_stop=True)