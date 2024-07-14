import avjoLangflowFunctions
import requests

"""Controller (app.py) call functions declared here for further processing"""


def getUser(user_id):
    url = f"http://127.0.0.1:5000/user/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return {"success": True, "data": user_data}

    elif response.status_code == 404:
        print(f"User {user_id} not found.")
        return {"success": True, "data": None}
    else:
        print(f"Failed to fetch user {user_id}. Status code: {response.status_code}")
        return {"success": False, "data": None}


def checkDocService(userId):
    """Retreive from DB if user has uploaded documents or not"""
    response = getUser(user_id=userId)

    if response.get["success"] and response.get["data"] != None:
        return True
        # user_data = response.get["data"]
        # context = user_data.get["context"]
        # if context is None:
        #     print(f"User {userId}'s bio is not provided.")
        # else:
        #     print(f"User {user_id}'s bio: {bio}")
    # result = "Documents are uploaded"
    return False


def getContextService(userId):
    """Retrieve data from DB of userId, and generate conetxt from data+user query"""
    # Get data in string format from DB
    user_data = getUser(user_id=userId)
    context = user_data["context"]

    # context = avjoLangflowFunctions.getContextLangflow(data, userQuery)
    return context


def checkFraudService(situation):
    """Check from the RAG model if the sitaution is Fraud and generate more information about the situation accordingly"""

    fraudContext = avjoLangflowFunctions.generateFraudContext(situation)
    return fraudContext


def triggerEmailService(userName, address, contactNo, situation):
    """Generate email from provided data, with the help of langflow agent, and trigger email to cyber dept."""

    subject, body = avjoLangflowFunctions.generateEmailLangflow(
        userName, address, contactNo, situation
    )

    # Trigger email to cyber dept mailId

    return "Email Triggered"
