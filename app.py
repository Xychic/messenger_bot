#Python libraries that we need to import for our bot
import os
from datetime import datetime
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

data = [1,2,3,4,5]

functionDescription = {
	"LIST-ALL" : "Will list all data and functions",
	"LIST-FUNC" : "Will list all functions",
	"LIST-DATA" : "Will list all data",
        "ECHO" : "Will repeat the message back"
}

def listAll(inputData):
    result = "FUNCTIONS"
    for function in functionDescription:
        result += "\n" + function + " : " + functionDescription[function]
    result += "\nDATA"
    for datum in data:
        result += "\n" + str(datum)
    return result

def listFunc(inputData):
    result = "FUNCTIONS"
    for function in functionDescription:
        result += "\n" + function + " : " + functionDescription[function]
    return result

def listData(inputData):
    result = "DATA"
    for datum in data:
        result += "\n" + str(datum)
    return result

def echo(inputData):
    return ("Received '{0}' at {1}").format(" ".join(inputData), str(datetime.now()))

functionAction = {
	"LIST-ALL" : listAll,
	"LIST-FUNC" : listFunc,
	"LIST-DATA" : listData,
        "ECHO" : echo
}


#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message(message['message'].get('text'))
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message(receivedText = "No text"):
    blocks = receivedText.split(" ")
    if blocks[0].upper() in functionAction:
        result = functionAction[blocks[0].upper()](blocks[1:])
    else:
        result = """ERROR:
Unknown command:'{0}'
Type 'LIST-FUNC' for a full list of possible commands""".format(receivedText)
    return result

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
