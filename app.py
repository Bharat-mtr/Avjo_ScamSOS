from flask import Flask, request, jsonify
from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route('/checkDoc', methods=['POST'])
def checkDoc():
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]
    ''' Check if the documents are uploaded or not'''
    return jsonify("No documents Uploaded")

@app.route('/getContext', methods=['POST'])
def getContext():
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    '''Returns the context from the documents uploaded'''
    return jsonify("user got a call from CBI")

@app.route('/checkFraud', methods=['POST'])
def checkFraud():
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    '''Check from the RAG model if its a fraud and then conversate with user'''
    return jsonify("This has happened before its a fraud i see")

@app.route('/generateReport', methods=['POST'])
def generateReport():
    # Check for required headers
    if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]
    
    '''Generate a Report of the fraud & store it in DB'''
    return jsonify("Report generate check DB")