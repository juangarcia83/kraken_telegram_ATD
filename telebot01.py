import telebot
import kraken_lib

# Conexion con nuestro Bot
#Token = "6941911754:AAHr6gYLJEIsQVcf5JIa6C_SbshlPxBZ08Q"  #TOKEN OSCAR
Token = "6500901829:AAFHVJED3qfbMDsVLLMmXB3x6p0EX8gb2dk"   #TOKEN JUAN
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, acabas de inicializar el Bot del Proyecto Kraken")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Con  /precio puedes ver los distintos precios de las criptomonedas, y con /lista las que hay")

@bot.message_handler(commands=['precio'])
def obtener_precio(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Por favor, proporciona el nombre de la criptomoneda y la divisa. Por ejemplo: /precio XXBTZUSD')
        return

    pair = message.text.split()[1].upper()
    price = kraken_lib.precio_crypto(pair)
    
    bot.reply_to(message, f'El precio de {pair} es ${price}')

@bot.message_handler(commands=['lista'])
def listar_crypto(message):
    available_cryptos = kraken_lib.lista_crypto()
    crypto_list = ", ".join(available_cryptos)
    bot.reply_to(message, f'Lista de las Crypto aviables en Kraken:\n{crypto_list}')

@bot.message_handler(commands=['data'])
def intercambios(message):
    cripto = message.text.split()[1].upper()
    intercambio = kraken_lib.intercambios(cripto)
    bot.reply_to(message, f'Los ults. intercambios son {intercambio[1]} @ ${float(intercambio[1])/float(intercambio[0])}')

"""
@bot.message_handler(commands=['baratos'])
def menores10(message):
    cryptos = kraken_lib.obtener_10_menores_valores()
    bot.reply_to(message,f"Las 10 Crypto mas baratas actualmente en Kraken:{cryptos}")
"""
# Polling para el bot de Telegram
    
bot.polling()
