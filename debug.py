from datetime import datetime

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
	
def get_message(receivedText = "No text"):
    blocks = receivedText.split(" ")
    if blocks[0].upper() in functionAction:
        result = functionAction[blocks[0].upper()](blocks[1:])
    else:
        result = """ERROR:
Unknown command:'{0}'
Type 'LIST-FUNC' for a full list of possible commands""".format(receivedText)
    return result

reponse = ""
while True:
    print(get_message(input()))
