from datetime import datetime
from random import randint

data = [1,2,3,4,5]
functionDescription = {
	"LIST-ALL" : "Will list all data and functions",
	"LIST-FUNC" : "Will list all functions",
	"LIST-DATA" : "Will list all data",
        "ECHO" : "Will repeat the message back",
        "REPEAT" : "Will repeat commands",
        "RANDINT" : "Generates a random number"
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

def repeat(inputData):
    result = """ERROR:
Unknown command:'{0}'
Type 'LIST-FUNC' for a full list of possible commands""".format(" ".join(inputData))
    try:
        repeats = int(inputData[-1])
        inputData = inputData[:-1]
        if inputData[0].upper() in functionAction:
            result = ""
            for i in range(repeats):
                if i != 0:
                    result += "\n"
                result += functionAction[inputData[0].upper()](inputData[1:])
    except Exception as e:
        result = """ERROR:
INVALID ARGUMENT:'{0}'
EXPECTED "FUNCTION" "INPUT" "REPEATS" """.format(" ".join(inputData))
    return result

def random(inputData):
    return str(randint(0,1000))
        

functionAction = {
	"LIST-ALL" : listAll,
	"LIST-FUNC" : listFunc,
	"LIST-DATA" : listData,
        "ECHO" : echo,
        "REPEAT" : repeat,
        "RANDINT" : random
}
