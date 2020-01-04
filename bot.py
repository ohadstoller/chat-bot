from chatterbot import ChatBot
# import nltk
import ssl
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# ntlk download()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context




bot = ChatBot(
    'SQLMemoryTerminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)
    # logic_adapters=[
    #     {
    #         'import_path': 'chatterbot.logic.BestMatch',
    #
    #         'default_response': 'I am sorry, but I do not understand.',
    #         'maximum_similarity_threshold': 0.90
    #     }
    # ]
    # logic_adapters=[
    #
    #     'chatterbot.logic.MathematicalEvaluation',
    #     # 'chatterbot.logic.TimeLogicAdapter',
    #     'chatterbot.logic.BestMatch'
    # ]


# Get a few responses from the bot

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m "Boto". Nice to meet you!']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']


list_trainer = ListTrainer(bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')


def ai_bot(q):
    return bot.get_response(q)

