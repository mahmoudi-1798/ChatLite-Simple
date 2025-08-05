# ChatLite - Minimalistic Web Chat Interface

A clean, modern web-based chat interface built with FastAPI and designed for AI interactions. This project provides a minimalistic yet powerful chat interface that can be easily integrated with any LLM backend.

## Features

- 🎨 Clean, modern UI with dark theme
- 💬 Real-time chat interface
- ⌨️ Auto-expanding input field
- ⚡ Fast and responsive design
- 🔄 Smooth scrolling and animations
- 📱 Mobile-friendly layout
- 🎯 Fixed input at bottom (like ChatGPT)
- 💫 Typing indicators
- 🎯 Modular architecture for easy LLM integration

## Project Structure

```
Simple-Chat-Page/
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css      # Styles for the chat interface
│   ├── templates/
│   │   └── index.html         # Main chat interface template
│   ├── llm/
│   │   └── llm_response.py    # LLM integration module
│   └── main.py               # FastAPI application
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Simple-Chat-Page
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open your browser and navigate to `http://localhost:8000`

## How It Works

### Frontend (HTML/CSS/JavaScript)
- The interface is built with vanilla HTML, CSS, and JavaScript
- CSS is separated into its own file for better maintainability
- The chat interface features a fixed header, scrollable chat area, and fixed input at bottom
- Messages are dynamically added to the chat box
- Auto-expanding textarea for comfortable message input
- Smooth scrolling and animations for better UX

### Backend (FastAPI)
- FastAPI serves as the web framework
- Static files (CSS) are served from the `app/static` directory
- Templates are served from the `app/templates` directory
- Two main endpoints:
  - `GET /`: Serves the main chat interface
  - `POST /chat`: Handles message processing and returns AI responses

### LLM Integration
- The `llm_response.py` module is designed to be easily integrated with any LLM
- Currently includes a mock response system for testing
- Can be replaced with actual LLM integration (e.g., OpenAI, Anthropic, etc.)

## Customization

### Styling
- Colors and themes can be modified in `app/static/css/style.css`
- The interface uses a dark theme by default but can be easily modified
- Font sizes, spacing, and other visual elements can be adjusted in the CSS

### LLM Integration
To integrate with an actual LLM:
1. Modify `app/llm/llm_response.py`
2. Add your LLM API keys to a `.env` file
3. Implement the actual API calls in the `get_llm_response` function

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 