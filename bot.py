import telebot
from config import TOKEN
from logic import get_class


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    car_name, percentage = get_class(image_path=file_name)
    bot.send_message(message.chat.id, f'С вероятностью {percentage}% на фото {car_name.lower()}')

bot.infinity_polling()
