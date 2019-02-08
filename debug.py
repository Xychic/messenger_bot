import functions

def get_message(receivedText = "No text"):
    blocks = receivedText.split(" ")
    if blocks[0].upper() in functions.functionAction:
        result = functions.functionAction[blocks[0].upper()](blocks[1:])
    else:
        result = """ERROR:
Unknown command:'{0}'
Type 'LIST-FUNC' for a full list of possible commands""".format(receivedText)
    return result

reponse = ""
while True:
    print(get_message(input()))
