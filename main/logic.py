import requests
import json
from promt import SYSTEM_PROMPT

def generate_ai_content(metadata):
    url = "http://localhost:11434/api/generate"
    
    full_prompt = f"{SYSTEM_PROMPT}\n\nВот данные для анализа:\n{json.dumps(metadata, ensure_ascii=False)}"
    
    payload = {
        "model": "llama3", # убедись, что модель скачана
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json().get('response', 'Ошибка генерации')
    except Exception as e:
        return f"Ошибка подключения к Ollama: {e}"
