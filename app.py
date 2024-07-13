from flask import Flask, request, jsonify
from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import os
import avjoService
load_dotenv()
app = Flask(__name__)

@app.route('/checkDoc', methods=['POST'])
def checkDoc():
    ''' Check if the documents are uploaded or not'''
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if "user id" not in args:
        return jsonify({"error": "Missing 'user id' in request body"}), 400
    
    result = avjoService.checkDocService(args["user id"])
    
    return jsonify("No documents Uploaded")

@app.route('/getContext', methods=['POST'])
def getContext():
    '''Returns the context from the documents uploaded'''

    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if "user query" not in args:
        return jsonify({"error": "Missing 'user query' in request body"}), 400
    
    if "user id" not in args:
        return jsonify({"error": "Missing 'user id' in request body"}), 400
    
    context = avjoService.getContextService(args["user id"], args["user query"])

    return jsonify(context)

@app.route('/checkFraud', methods=['POST'])
def checkFraud():
    '''Check from the RAG model if its a fraud and then conversate with user'''
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if 'situation' not in args:
        return jsonify({"error": f"Missing situation in request body"}), 400
    
    fraudContext = avjoService.checkFraudService(args['situation'])

    
    return jsonify("This has happened before its a fraud i see")

@app.route('/triggerEmail', methods=['POST'])
def triggerEmail():
    '''Generate and Trigger Email of Cyber Department'''
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]
    # name, address, contact number, awb number, breif overview of situation
    req_inp= ["user name", "address", "contact no", "situation"]
        
    for inp in req_inp:
        if inp not in args:
            return jsonify({"error": f"Missing {inp} in request body"}), 400

    if "awb no" not in args:
        args["awb no"] = None    
        
    avjoService.triggerEmailService(args["user name"], args["address"],args["contact no"],args["awb no"],args["situation"])

@app.route('/generateReport', methods=['POST'])
def generateReport():
    '''Generate a Report of the fraud & store it in DB'''
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    
    return jsonify("Report generate check DB")