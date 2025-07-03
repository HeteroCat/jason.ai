# Jason's AI World

A Streamlit-based personal portfolio showcasing various AI experiments and demos.

## Features

- **Homepage** (`Hello.py`)
  - Personal resume and project highlights
- **Avatar Demo** (`pages/Avatar_Demo.py`)
  - Chat with a Coze-powered digital persona
- **Data Demo** (`pages/Data_Demo.py`)
  - Upload PDFs or CSV for Q&A and data visualization powered by LangChain and FAISS
- **Sarcasm Demo** (`pages/Sarcasm_Demo.py`)
  - Example chatbot with a snarky personality powered by Dify
- **Game Chat Demo** (`pages/gamechat_Demo.py`)
  - Interactive history adventure using the OpenAI API

## Installation

1. Install Python 3.9 or newer.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

From the repository root run:

```bash
streamlit run Hello.py
```

Use the sidebar to navigate between demo pages. Some demos require API keys which can be entered via the sidebar.

## Repository Layout

```
├── Hello.py             # Main entry page
├── pages/               # Demo pages
├── utils.py             # Shared helpers
├── requirements.txt     # Package list
├── faiss_db/            # Vector index used by Data Demo
└── various images
```
