# Real-Time Translation App

Local LLM-powered translation using **Jan.ai** as the backend.

## Setup

### 1. Install dependencies

```bash
cd translate-app
pip install -r requirements.txt
```

### 2. Configure

Edit `app.py` — change these if needed:

```python
JAN_BASE_URL = "http://localhost:1337/v1"  # Jan's API endpoint
MODEL_NAME = "gemma-4-E2B-it"              # Your model name in Jan
```

### 3. Start Jan.ai

1. Open Jan.ai app
2. Load your model (e.g., `gemma-4-E2B-it`)
3. Make sure the local server is enabled

### 4. Run

```bash
cd translate-app
python app.py
```

Open **http://localhost:7860** in your browser.

## Features

- 🌐 30+ languages
- ⚡ Real-time streaming (tokens appear as generated)
- 🔄 Swap languages instantly
- 🔒 100% local — data never leaves your machine
