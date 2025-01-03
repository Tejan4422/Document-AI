import requests
import json
import time
from google.auth import default
from google.auth.transport.requests import Request
from google.auth.exceptions import GoogleAuthError
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
from google.colab import auth
#from google.cloud import discoveryengine_v1 as discoveryengine
import json
import requests
from google.cloud import firestore, bigquery
from datetime import datetime
import hashlib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from google.cloud import documentai_v1beta3 as documentai

# Authenticate the user
auth.authenticate_user()

# Function to get the access token for authentication
def get_access_token():
    credentials, _ = default()
    credentials.refresh(Request())
    return credentials.token

# TODO(developer): Update and un-comment below line
project_id = "veefin-ai-426106"

#vertexai.init(project=project_id, location = "us-central1")

location = ''
processor_id = ''  # Replace with your processor ID
processor_name = f'projects/{project_id}/locations/{location}/processors/{processor_id}'





"""# Document AI API Implementation"""

import requests
import base64
from google.auth import default
from google.auth.transport.requests import Request

# Authenticate the user in Colab
from google.colab import auth
auth.authenticate_user()

# Function to get the access token for authentication
def get_access_token():
    credentials, _ = default()  # Get default credentials
    credentials.refresh(Request())  # Refresh credentials to get a valid token
    return credentials.token

# Define the prediction endpoint from your processor details
endpoint = ""

# Load the document file (e.g., PDF)
with open('/content/Financial-Examples-for-I20.pdf', 'rb') as file:
    document_content = file.read()

# Encode the document content to base64
encoded_document = base64.b64encode(document_content).decode('utf-8')

# Prepare the request payload with the base64-encoded content
data = {
    "rawDocument": {
        "content": encoded_document,
        "mimeType": "application/pdf"
    }
}

# Get the access token
access_token = get_access_token()

# Set up the authorization headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Send the request to the prediction endpoint
response = requests.post(endpoint, headers=headers, json=data)

# Process and display the response
if response.status_code == 200:
    response_data = response.json()
    print("Document processed successfully!")
    # Example of how to process and display extracted entities
    if 'document' in response_data and 'entities' in response_data['document']:
        for entity in response_data['document']['entities']:
            print(f"Entity: {entity['type']}, Value: {entity['mentionText']}")
    else:
        print("No entities found in the response.")
else:
    print(f"Error: {response.status_code}, {response.text}")

