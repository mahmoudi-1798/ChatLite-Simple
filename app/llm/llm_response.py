# Import required libraries
from typing import Optional, AsyncGenerator
import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import json

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize LangChain chat model with streaming
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    streaming=True,
    api_key=os.getenv("OPENAI_API_KEY")
)

async def get_llm_response(message: str) -> AsyncGenerator[str, None]:
    """
    Process user message and stream AI response using LangChain.
    
    Args:
        message (str): The user's input message
        
    Yields:
        str: Chunks of the AI's response
    """
    try:
        if not validate_api_key():
            yield "Error: OpenAI API key not configured. Please check your .env file."
            return

        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content=message)
        ]
        
        # Stream the response token by token
        async for chunk in chat.astream(messages):
            if hasattr(chunk, 'content'):
                content = chunk.content
                if content and isinstance(content, str):
                    yield content
            elif hasattr(chunk, 'text'):
                text = chunk.text
                if text and isinstance(text, str):
                    yield text

    except Exception as e:
        # Log the error and yield a user-friendly message
        print(f"Error in get_llm_response: {str(e)}")
        yield "I apologize, but I'm having trouble processing your request at the moment. Please try again later."

def validate_api_key() -> bool:
    """
    Validate if the OpenAI API key is properly configured.
    
    Returns:
        bool: True if API key is valid, False otherwise
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in environment variables")
        return False
    return True 