# Calorie Chatbot 🍎🤖

A Python-based chatbot that estimates calories based on user food entries.  
Built with a clean UI (ttkbootstrap), SQLite database, and FastAPI backend for easy integration.

## 🚀 Features
- **`chat.py`** – `responding(input_str)` uses Gemini API to return calorie estimates.  
- **`database.py`** – SQLite functions:  
  - `alldata()`  
  - `add_entry(date, value)`  
  - `get_entry(date)`  
  - `update_entry(date, value)`  
  - `delete_entry(date)`  
- **`ui.py`** – Beautiful desktop UI using **ttkbootstrap**.  
- **`server.py`** – FastAPI server for remote connections.

