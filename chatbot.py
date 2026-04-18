import json
from chatterbot import ChatBot

#reading the json inputs
def readjson(filename):
    data_file = open(filename).read()
    intents = json.loads(data_file)
    print (  intents["intents"])
    intentsdata=[]
    for data in intents["intents"]:
        print("Name:", data['question'])
        intentsdata.append(data['question'])
        print("answer:", data['answer'])
        intentsdata.append(data['answer'])
    print (intentsdata)
    return intentsdata


chatbot = ChatBot(
    'NekBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    # database_uri='sqlite:///database.sqlite3'
)

personaljson = readjson('training_data/personal_ques.json')
questionjson = readjson('training_data/ques_ans.json')
# data_file = open('training_data/personal_ques.json').read()
# intents = json.loads(data_file)
# print (  intents["intents"])
# intentsdata=[]
# for data in intents["intents"]:
#     print("Name:", data['question'])
#     intentsdata.append(data['question'])
#     print("Website:", data['answer'])
#     intentsdata.append(data['answer'])
# print (intentsdata)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

#training_data = training_data_quesans + training_data_personal + intentsdata
training_data = personaljson + questionjson 

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english','chatterbot.corpus.english.greetings','chatterbot.corpus.english.conversations'
) 
