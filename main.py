import config
import answer
import core
import telebot
import tweepy
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
client = tweepy.Client(bearer_token=config.x_bearer_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, get_latest_tweets())
    bot.send_message(message.chat.id, answer.TEXT_WELCOME_USERS, reply_markup=types.ReplyKeyboardRemove())

def get_latest_tweets():
    try:
        response = client.get_users_tweets(id='44196397', max_results=5) # Elon Musks user id (for testing)
        tweets = response.data
        tweets_text = "\n\n".join([f"@elonmusk said: {tweet.text}" for tweet in tweets])
        return tweets_text
    except Exception as e:
        return f"Error: {e}"

def get_user_id(username):
    try:
        user = client.get_user(username=username)
        return user.data.id
    except Exception as e:
        return f"Error: {e}"

bot.polling(none_stop=True)