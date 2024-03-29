from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI, OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()


def get_llm():
    # Initialize the model
    return OpenAI()


def get_chat_model():
    # Initialize the model
    return ChatOpenAI()


def get_embeddings():
    return OpenAIEmbeddings()
