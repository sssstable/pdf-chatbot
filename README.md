# Streamlit PDF Chatbot

This is a Streamlit app that allows you to chat with the content of a PDF file. It uses Langchain for language processing and Neo4j for vector storage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamlit-pdf-chatbot.git
   cd streamlit-pdf-chatbot
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your environment variables.

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Upload a PDF file and start asking questions about its content.

## Folder Structure

```
streamlit-pdf-chatbot/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── chains.py
└── data/
    └── pdfs/
        └── sample.pdf
```
