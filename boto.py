from bottle import route, run, template, static_file, request
import random
import json
import profanity_check
import bot
import joke


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps(check_bad_words(user_message))

def check_bad_words(user_message):
    input_check = profanity_check.predict([user_message])
    joke_list = ["joke", "Joke", "funny"]
    split_array = user_message.split()

    if input_check == 0 and any(x in joke_list for x in split_array):
        funny_animations = ['laughing', 'giggling']
        random_funny_animation = random.choice(funny_animations)
        tell_a_joke = joke.random_joke()
        return {"animation": random_funny_animation, "msg": tell_a_joke}

    if input_check != 0:
        bad_animations = ['afraid', 'crying', 'heartbroke', 'confused']
        random_bad_animation = random.choice(bad_animations)
        return {"animation": random_bad_animation, "msg": "please don't use this language"}

    else:
        good_animations = ['excited', 'dancing', 'inlove', 'ok']
        random_good_animation = random.choice(good_animations)
        bot_msg = bot.ai_bot(user_message)
        return {"animation": random_good_animation, "msg": str(bot_msg)}



@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": ""})
# return json.dumps(reply.reply(user_message)

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
