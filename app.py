import os
#pip install adafruit-io
from Adafruit_IO import Client
username_1= os.getenv('username')
key_1= os.getenv('key')
aio = Client(username_1,key_1)
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning on the Light')
  aio.send('light',1)

def demo2(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning off the Light')
  aio.send('light',0)
  
def demo3(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning on the Fan')
  aio.send('fan',1)

def demo4(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning off the Fan')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a=='lights on' or a=='turn on lights' or a=='turn lights on' or a=='turn on light' or a=='on light' or a=='light on' or a=='on lights' or a=='turn light on' :
    demo1(bot,update)
  elif a=='lights off' or a=='turn off lights' or a=='turn lights off' or a=='turn off light' or a=='off light' or a=='light off' or a=='off lights' or a=='turn light off'  :
    demo2(bot,update)
  elif a=='fans on' or a=='turn on fans' or a=='turn fans on' or a=='turn on fan' or a=='on fan' or a=='fan on' or a=='on fans' or a=='turn fan on' :
    demo3(bot,update)
  elif a=='fans off' or a=='turn off fans' or a=='turn fans off' or a=='turn off fan' or a=='off fan' or a=='fan off' or a=='off fans' or a=='turn fan off' :
    demo4(bot,update)

bot_token ='2046009698:AAErk31YPE8ujNPihuO5HTDZplbpSNk5WiU'
u = Updater(bot_token,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

