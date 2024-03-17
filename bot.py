import os

import telebot
import scraping

# BOT_TOKEN = "6400351145:AAGB06Pr1Q14WL0x0EifL3nksbqeKMPi8U4"
BOT_TOKEN = "6400351145:AAGB06Pr1Q14WL0x0EifL3nksbqeKMPi8U4"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start' , "hello"])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang! Saya adalah layanan bot pencari link route kendaraan umum. Mohon masukkan jenis kendaraan yang Anda inginkan untuk memulai pencarian")



@bot.message_handler(commands=['lrt' , 'krl' , 'mrt' , 'busway'])
def send_response(message):
    command = message.text.replace('/' , '');
    bot.reply_to(message , 'Permintaan diterima, tunggu sebentar yaa')
    links = scraping.scarping(command)
    if links:
        bot.reply_to(message, "Berikut adalah hasil link route pencarian anda ⬇️")
        for link in links:
            bot.reply_to(message, link)
        bot.reply_to(message, "Terimakasih, semoga harimu menyenangkan! 😊")
    else:
        bot.reply_to(message, "Maaf, tidak ada hasil yang ditemukan untuk perintah tersebut.")
    
bot.infinity_polling()