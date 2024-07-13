import avjoLangflowFunctions
'''Controller (app.py) call functions declared here for further processing'''

def checkDocService(userId):
    '''Retreive from DB if user has uploaded documents or not'''

    result = "Documents are uploaded"
    return result

def getContextService(userId, userQuery):
    '''Retrieve data from DB of userId, and generate conetxt from data+user query'''
    #Get data in string format from DB

    context = avjoLangflowFunctions.getContextLangflow(data, userQuery)
    return context

def checkFraudService(situation):
    '''Check from the RAG model if the sitaution is Fraud and generate more information about the situation accordingly'''
    
    fraudContext = avjoLangflowFunctions.generateFraudContext(situation)
    return fraudContext

def triggerEmailService(userName, address, contactNo, situation):
    '''Generate email from provided data, with the help of langflow agent, and trigger email to cyber dept.'''
    
    subject, body = avjoLangflowFunctions.generateEmailLangflow(userName, address, contactNo, situation)

    #Trigger email to cyber dept mailId
    
    return "Email Triggered"
