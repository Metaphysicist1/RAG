# Import the Pinecone library
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os


load_dotenv()
# Initialize a Pinecone client with your API key
pc = Pinecone(api_key=os.getenv("PINECONE_KEY"))



