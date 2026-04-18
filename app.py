from chatbot import chatbot

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(chatbot.get_response(userText))
    print ("response = " + botReply)
    if botReply.find("current time") > 0:
        botReply = str('I am sorry, but I do not understand. I am still learning.')
    return botReply


if __name__ == "__main__":
    app.run()