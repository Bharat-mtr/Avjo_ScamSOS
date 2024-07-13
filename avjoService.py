import avjoLangflowFunctions
'''Controller (app.py) call functions declared here for further processing'''

def getContextService(userId, userQuery):
    '''Retrieve data from DB of userId, and generate conetxt from data+user query'''
    #Get data in string format from DB

    context = avjoLangflowFunctions.getContextLangflow(data, userQuery)
    return context