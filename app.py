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
    
    context = avjoService.getContextService(args["user query"])

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

    
    return jsonify("This has happened before its a fraud i see")

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