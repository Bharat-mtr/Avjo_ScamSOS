''' Contains Langflow functions, avjoService call langflow functions described here, for langflow agent'''

from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import os
import re


def generateFraudContext(situation): 
    TWEAKS = {
    "ChatInput-40XjM": {},
    "AstraVectorStoreComponent-ZFB1J": {},
    "ParseData-PAkjS": {},
    "Prompt-0uaUQ": {},
    "ChatOutput-7wD60": {},
    "SplitText-PJbX9": {},
    "File-Mdai7": {},
    "AstraVectorStoreComponent-Ape61": {},
    "OpenAIEmbeddings-BV0CR": {},
    "OpenAIEmbeddings-Al7qh": {},
    "OpenAIModel-meCEK": {}
    }

    result = run_flow_from_json(flow="Check Fraud RAG.json",
                                input_value=situation,
                                fallback_to_env_vars=False, # False by default
                                tweaks=TWEAKS)
    
    context = result[0].outputs[0].results['message'].data['text'] 
    return context

def generateEmailLangflow(userName, address, contactNo, situation): 
    input_value = {"User Name":userName,"Address":address,"Contact Number":contactNo,"Situation":situation}
    TWEAKS = {
    "ChatInput-txKLO": {},
    "Prompt-utnqo": {},
    "ChatOutput-M9G2v": {},
    "OpenAIModel-PgEba": {}
    }

    result = run_flow_from_json(flow="Email Generator.json",
                                input_value=str(input_value),
                                fallback_to_env_vars=False, # False by default
                                tweaks=TWEAKS)
    
    output = result[0].outputs[0].results['message'].data['text']
    subject_match = re.search(r'<subject>(.*?)</subject>', output, re.DOTALL)
    subject = subject_match.group(1).strip() if subject_match else ''

    # Extract body
    body_match = re.search(r'<body>(.*?)</body>', output, re.DOTALL)
    body = body_match.group(1).strip() if body_match else ''

    return subject, body