from bs4 import BeautifulSoup
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

#парсер
# url = 'https://www.sberbank.ru/ru/person/credits/homenew'
# requests = requests.get(url)
# soup = BeautifulSoup(requests.text, 'html.parser')
# print(soup)

#Переменная бота
bot = Bot(token='5570768956:AAHd7hwxRVhqG1hdeglx6SQWtmxm9v-ILYY')

# диспетчер
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(f'Привет, {message.from_user.full_name}!')


#Прием сообщений
@dp.message_handler() #все сообщения
async def get_message(message: types.Message):
    # получаем айди пользователя
    chat_id = message.chat.id
    #текст, которым будет отвечать бот
    # text = 'какой-то текст'
    #text = f'Hi {message.from_user.full_name}'
    # await bot.send_message(chat_id=chat_id, text=text)
    #2 вариант
    #text = message.text
    await message.answer(text=chat_id)#text)

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Новостройка": "Ставка от 9,9%, Первый взнос от 0% \U00002600",
        "Вторжилье": "Ставка от 9,9%, Первый взнос от 0% \U00002601",
        "С госсподдержкой": "Ставка от 6,3%, Первый взнос от 15% \U00002614",
        "Семейная": "Ставка от 5,3%, Первый взнос от 15% \U00002614",

    }


executor.start_polling(dp)

#Прогноз погоды
# def get_weather(city, bot):
#     try:
#     except Exception as ex:
#         print(ex)
#         print('Проверьте название города')
#
# def main():
#     city = input('Введите город')
#     get_weather(city, bot)
#
# if __name__ == '__main__':
#     main()