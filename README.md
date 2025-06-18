# Jason's AI World

This repository contains a personal portfolio and AI demo collection built with [Streamlit](https://streamlit.io/). The project showcases various experiments with large language models and generative tools. Each demo is accessible as a page in the Streamlit app.

## Features

- **Homepage** (`Hello.py`)
  - Introduction and personal resume information
  - Links to AI projects and contact details
- **Dify Chatbot Demo** (`pages/Dify_Demo.py`)
  - Chat interface powered by the Dify API
- **Coze Demo** (`pages/coze_Demo1.py`)
  - Example integration with the Coze API
- **Game Chat Demo** (`pages/gamechat_Demo.py`)
  - Text adventure built on the OpenAI API
- **AI Music** (`pages/My_AI_music.py`)
  - Showcases music generated via Suno AI
- **AI Picture** (`pages/My_AI_picture.py`)
  - Displays images created for an AIGC contest
- **To‑do List** (`pages/To do list.py`)
  - Simple to‑do list implemented with embedded HTML/JS

## Installation

1. Ensure Python 3.9+ is installed.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application from the repository root:

```bash
streamlit run Hello.py
```

The navigation sidebar lists all available demo pages.

## Repository Layout

```
├── Hello.py          # Main page
├── pages/            # Additional demo pages
├── utils.py          # Shared helper functions
├── requirements.txt  # Python dependencies
└── images and other media files
```

Feel free to explore the code and customize the demos for your own experiments.
