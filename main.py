from telebot import TeleBot
from telebot import types

token = '6251340110:AAH7a-23NsXz3943l18OLebEIjQj7FOhPQY'
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	keyboard = types.InlineKeyboardMarkup()
	url_btn = types.InlineKeyboardButton(text="Хочу урок 1", callback_data='lesson1')
	keyboard.add(url_btn)
	bot.send_message(message.from_user.id, F'Привет {message.from_user.first_name}!\nМеня зовут Мирослава Чиж @miroslava_chizh - пиши мне по всем вопросам!\n\nЯ хочу подарить тебе Новый Завет Сетевика! 🎁Это твоя карта в мир красивого сетевого! \n\n‌В этой инструкции я даю алгоритм системы АВТОВОРОНКА. ПОТОК ВХОДЯЩИХ \n👇👇👇👇👇\nhttps://drive.google.com/file/d/1xZrNQ6VvYAPPynTOvIjCG2mslwa87vNP/view?usp=sharing\n\nБлагодаря ей, ты сможешь научиться легко получать 5 регистраций в день, при этом люди будут писать тебе сами!\n\nПока изучай инструкцию, а через 24 часа, я пришлю короткое, но очень полезное видео, в котором наглядно объясню всю систему получения от 5 входящих в день!', reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
	if call.data == 'lesson1':
		keyboard = types.InlineKeyboardMarkup()
		url_btn = types.InlineKeyboardButton(text="Хочу урок 2", callback_data='lesson2')
		keyboard.add(url_btn)
		bot.send_message(call.from_user.id, "Как получать 5 входящих в день?\nЕще раз привет 🤗\nНу что ж, пришло время посмотреть первый урок\n👇👇👇👇👇👇\nhttps://youtu.be/_91ulNKh6r8\n\nКАК ПОЛУЧАТЬ 5 входящих в день без списков, звонков, 100\nстраниц, спама, покупки анкет, блокировок, уговоров и возражений?\nНадеюсь, тебе будет полезно! До встречи! Увидимся на следующий день на втором уроке\nСупер-упаковка - это на 100% решит проблемы с привлечением потенциальных\nпартнеров.", reply_markup=keyboard)
	elif call.data == 'lesson2':
		keyboard = types.InlineKeyboardMarkup()
		url_btn = types.InlineKeyboardButton(text="Хочу урок 3", callback_data='lesson3')
		keyboard.add(url_btn)
		bot.send_message(call.from_user.id, "Как упаковать себя в социальных сетях?\n\nПривет! Мирослава Чиж на связи, и мы продолжаем развиваться в сетевом.\nНе понимаешь, как вести соцсети так, чтобы партнеры сами просились в бизнес? Смотри\nвторое видео, оно уже доступно по ссылке\n👇👇👇👇👇\nhttps://youtu.be/u6702Os9kgs\n\nСегодня ты поймешь, как оформлять аккаунты так, чтобы они привлекали партнеров, даже\nкогда ты спишь. 😴\nЗдесь важна каждая мелочь, которая хотя бы 0,0001% будет склонять потенциального\nпартнера присоединиться в твою команду\n\n“Вкусная” упаковка на 100% решит проблемы с привлечением потенциальных партнеров.\nПриятного просмотра и до завт3ра!", reply_markup=keyboard)
	elif call.data == 'lesson3':
		keyboard = types.InlineKeyboardMarkup()
		url_btn = types.InlineKeyboardButton(text="Хочу урок 4", callback_data='lesson4')
		keyboard.add(url_btn)
		bot.send_message(call.from_user.id, "Контент и бесплатный трафик для привлечения партнеров\nНе получается создавать продающий контент? Не понимаешь, как привести первых\nподписчиков? 🤔\n\nПора познакомить тебя с одним из главных элементов моей системы – это контент и\nбесплатный трафик\nСмотри третье видео\n👇👇👇👇👇👇👇\nhttps://youtu.be/OkS5zbB9KbM\n\nИз него ты узнаешь, как:\n✅писать полезно-продающие посты\n✅получать входящий трафик бесплатно\n✅набрать первых подписчиков и начать приглашать на консультации.\n✅собрать еще больше лояльной аудитории, которую потом легко перевести в партнеры.\nЕще ты разберешься в 6 эффективных и бесплатных способах рекрутинга.\n\n‌Увидимся завтра!", reply_markup=keyboard)
	elif call.data == 'lesson4':
		keyboard = types.InlineKeyboardMarkup()
		url_btn = types.InlineKeyboardButton(text="Записатся на КОНСУЛЬТАЦИЮ", url="https://t.me/miroslava_chizh")
		keyboard.add(url_btn)
		bot.send_message(call.from_user.id, "🤳УЧУ ОБРАБАТЫВАТЬ ЗАЯВКИ ✅\n\nВот и дошла очередь до самого интересного видео! В уроке рассказала алгоритм\nпроведения консультации, чтобы 8 из 10 потенциальных партнеров сказали “Да, я хочу к вам в команду!\"\n\nВидео доступно по ссылке\n👇👇👇👇👇👇\nhttps://youtu.be/ahGNKBOibig\n\nПереходи по ссылке и скорее узнавай, как подготовиться к консультации так, чтобы она\nпрошла успешно.\n\nНачни регистрировать 8 человек из 10 в команду на 15 минутных консультациях\n\nЖми👇", reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)   
def echo_all(message):
	try:
		i = message.text.index("asdasd")
		bot.send_message(message.from_user.id, '????')
	except ValueError:
		pass
# if message.text:
# 	r = TeleBot.types.InlineQueryResultArticle('1', 'Result', TeleBot.types.InputTextMessageContent('Result message.'))
#     r2 = TeleBot.types.InlineQueryResultArticle('2', 'Result2', TeleBot.types.InputTextMessageContent('Result message2.'))
#     bot.answer_inline_query(inline_query.id, [r, r2])
# bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)
