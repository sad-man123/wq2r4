import telebot, code, pyVariable, os, zipfile

bot = telebot.TeleBot('7260587081:AAGIb_ye_QXgFk2T-LR8Jjvhx9f3vn41RvI')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        text = message.text
        fromm = message.json
        if os.path.exists("test"):
            with open("code.py", "w") as f:
                f.write(message.text)
                os.remove("test")
        if "123123_vn122" in text and fromm["from"]["is_bot"] == False:
            word_array = pyVariable.words(text)
            print(word_array)
            if word_array[1] == "start":
                word_array.remove(word_array[0])
                word_array.remove(word_array[1])
                code.main(word_array)
                bot.send_message(message.chat.id, "code start nice")
            if word_array[1] == "downland_code_text":
                bot.send_message(message.chat.id, "i'm ready")
                with open("test", "w") as test:
                    ...
    except Exception as ex:
        print(ex)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "safe is nice")
        with zipfile.ZipFile(src) as f:
            f.extractall("./")
        bot.reply_to(message, "extract is nice")
        os.remove(src)
    except Exception as e:
        bot.reply_to(message, e)


bot.infinity_polling(none_stop=True)