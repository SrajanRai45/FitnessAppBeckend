# ⚡ FastAPI Chat Server — Gemini Flash 2.0 Powered AI Backend

Welcome to the **FastAPI Chat Server**!  
This project provides a simple, extensible, and lightning-fast Python server designed to interact with AI using **Google’s Gemini Flash 2.0 API**.  
It works in sync with the **CPR-based C++ client** (available in your other GitHub repo), but can also be used independently by setting up your own responding function!

---

## ✨ Core Feature — `chat.py`

Inside the heart of this project lies:

### `chat.py` — the AI Connector

This file defines a function called `responding`, which is responsible for:

- Sending user input to **Gemini Flash 2.0** using your API key  
- Fetching a response from Gemini AI  
- Returning it in a usable format

> **Note:** The `responding` function **must be written by you** if not already implemented! The server is ready to host it, so you just need to plug in your own logic.

---

## 🔐 Environment Setup

Since we are dealing with the **Gemini API**, you'll need a `.env` file to store your API key **securely**.

### Create a `.env` file in your project root:

