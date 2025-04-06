# Flask Generative AI Chat Application

This repository provides a Flask-based web API that integrates with Google Generative AI (Gemini) for conversational chat functionality. Users can send queries to the `/chat` endpoint, and the application generates AI-powered responses using Gemini's Generative Model.

---

## Features

- **Endpoints**:
  - `/` - Welcome message endpoint.
  - `/chat` (POST) - Accepts a user query and generates a response using Gemini's Generative Model.
- **Integration with Google Generative AI**:
  - Leverages the Gemini API for text generation.
- **Error Handling**:
  - Handles missing inputs and exceptions gracefully.

---

## Requirements

Install the required Python packages using pip:

```bash
pip install flask flask-cors google-generativeai
