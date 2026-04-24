# 🌐 Real-Time Translation App

Local LLM-powered translation using **Jan.ai** as the backend. Your data stays on your machine.

## Requirements

- **Windows 11**
- **Jan.ai** installed with a model loaded (e.g., `gemma-4-E2B-it`)
- **Python 3.10+** ([download from python.org](https://www.python.org/downloads/))

## Setup

### 1. Install Python

Download Python 3.10+ from [python.org](https://www.python.org/downloads/windows/).

**Important**: During installation, check ✅ **Add Python to PATH**.

### 2. Clone or Download

```powershell
# If you have git
git clone https://github.com/TrentColOS/translate-app.git
cd translate-app

# Or download ZIP and extract
```

### 3. Install Dependencies

Open **Command Prompt** or **PowerShell** in the `translate-app` folder:

```powershell
pip install -r requirements.txt
```

### 4. Configure

Open `app.py` in a text editor (Notepad, VS Code, etc.) and check line 16:

```python
MODEL_NAME = "gemma-4-E2B-it"  # Change to your model name in Jan
```

Make sure this matches the model name shown in Jan.

### 5. Start Jan.ai

1. Open **Jan.ai**
2. Load your model (e.g., `gemma-4-E2B-it`)
3. Ensure the local server is running (Jan enables it by default)

### 6. Run

```powershell
python app.py
```

Open **http://localhost:7860** in your browser.

## Troubleshooting

### "Connection refused" error
- Make sure Jan.ai is running and the model is loaded
- Check that Jan's server port is `1337` (default)

### Model not found
- Open Jan and check the exact model name in your model list
- Update `MODEL_NAME` in `app.py` to match exactly

### pip not recognized
- Reinstall Python and check "Add Python to PATH"
- Or use: `py -m pip install -r requirements.txt`
