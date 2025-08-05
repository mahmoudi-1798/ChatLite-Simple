# Import required FastAPI components
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, StreamingResponse
from sse_starlette.sse import EventSourceResponse
import uvicorn
import asyncio
import json

# Import the LLM response function from our custom module
from app.llm.llm_response import get_llm_response

# Initialize FastAPI application
app = FastAPI()

# Mount the static directory to serve CSS, JS, and other static files
# This allows FastAPI to serve files from the app/static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 templates
# This tells FastAPI where to find our HTML templates
templates = Jinja2Templates(directory="app/templates")

# Root endpoint - serves the main chat interface
@app.get("/")
async def read_root(request: Request):
    """
    Serves the main chat interface.
    Args:
        request: The incoming HTTP request
    Returns:
        Rendered HTML template with the chat interface
    """
    return templates.TemplateResponse("index.html", {"request": request})

# Chat endpoint - handles message processing with streaming
@app.post("/chat")
async def chat(message: str = Form(...)):
    """
    Processes incoming chat messages and streams AI responses.
    Args:
        message: The user's message from the form
    Returns:
        StreamingResponse: Server-Sent Events stream of the AI's response
    """
    if not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    async def event_generator():
        try:
            async for chunk in get_llm_response(message):
                if chunk and isinstance(chunk, str):
                    # Ensure the chunk is a string and properly formatted
                    yield {
                        "event": "message",
                        "data": json.dumps({"data": chunk})
                    }
        except Exception as e:
            print(f"Error in event_generator: {str(e)}")
            yield {
                "event": "error",
                "data": json.dumps({"error": "An error occurred while generating the response"})
            }
    
    return EventSourceResponse(event_generator())

# Run the application if this file is executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 