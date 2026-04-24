"""
Real-time Translation App
Uses Jan.ai local server as the LLM backend
"""

import gradio as gr
from openai import OpenAI
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# CONFIG - Edit these to match your setup
# ============================================================
JAN_BASE_URL = "http://127.0.0.1:1337/v1"  # Jan.ai local server
MODEL_NAME = "gemma-4-E2B-it-Q8_0"  # Change to your model name in Jan
# ============================================================

client = OpenAI(
    api_key="not-needed",  # Jan doesn't require auth locally
    base_url=JAN_BASE_URL,
)

SYSTEM_PROMPT = """You are a professional translator. You translate text accurately and naturally.
Rules:
- Only output the translation, nothing else
- Preserve the meaning and tone of the original text
- Keep numbers and proper nouns as-is
- Do not add explanations or notes"""

LANGUAGES = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese",
    "Russian", "Chinese", "Japanese", "Korean", "Arabic", "Hindi",
    "Dutch", "Polish", "Turkish", "Vietnamese", "Thai", "Indonesian",
    "Greek", "Czech", "Swedish", "Danish", "Norwegian", "Finnish",
    "Hebrew", "Ukrainian", "Romanian", "Hungarian", "Bulgarian", "Croatian"
]

def translate_stream(text, src_lang, tgt_lang):
    """Stream translation from Jan.ai"""
    if not text.strip():
        return ""

    prompt = f"""Translate from {src_lang} to {tgt_lang}.

{src_lang}: {text}
{tgt_lang}:"""

    try:
        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            max_tokens=2048,
            stream=True,
        )

        result = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                result += token
                yield result

    except Exception as e:
        yield f"Error: {str(e)}\n\nMake sure Jan.ai is running at {JAN_BASE_URL} with a model loaded."

def build_ui():
    with gr.Blocks(
        title="Translate",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="gray",
        )
    ) as app:
        gr.Markdown("""
        # 🌐 Real-Time Translation
        Powered by **Jan.ai** local LLM — your data stays on your machine.
        """)

        with gr.Row():
            with gr.Column(scale=1):
                src_lang = gr.Dropdown(
                    choices=LANGUAGES,
                    value="English",
                    label="From",
                    allow_custom_value=False,
                )

            with gr.Column(scale=1):
                tgt_lang = gr.Dropdown(
                    choices=LANGUAGES,
                    value="French",
                    label="To",
                    allow_custom_value=False,
                )

        with gr.Row():
            src_text = gr.Textbox(
                label="Enter text",
                placeholder="Type or paste text to translate...",
                lines=8,
                scale=1,
            )

            output_text = gr.Textbox(
                label="Translation",
                lines=8,
                scale=1,
                interactive=False,
            )

        swap_btn = gr.Button("🔄 Swap Languages", size="sm")

        def swap(l1, l2):
            return l2, l1

        swap_btn.click(
            fn=swap,
            inputs=[src_lang, tgt_lang],
            outputs=[src_lang, tgt_lang],
        )

        translate_btn = gr.Button("Translate", variant="primary", size="lg")

        translate_btn.click(
            fn=translate_stream,
            inputs=[src_text, src_lang, tgt_lang],
            outputs=output_text,
        )

        src_text.submit(
            fn=translate_stream,
            inputs=[src_text, src_lang, tgt_lang],
            outputs=output_text,
        )

        gr.Markdown("""
        ---
        **Tips:**
        - Press Enter to translate instantly
        - Click 🔄 to swap source/target languages
        - Make sure Jan.ai is running with a model loaded
        """)

    return app

if __name__ == "__main__":
    print(f"\n🌐 Translation App")
    print(f"   Jan.ai endpoint: {JAN_BASE_URL}")
    print(f"   Model: {MODEL_NAME}")
    print(f"\n   Open: http://localhost:7860\n")

    app = build_ui()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )
