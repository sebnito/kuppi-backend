KEYWORD_MAP = {
    "weather": ["อากาศ", "ฝน", "ร้อน", "หนาว", "พยากรณ์", "อุณหภูมิ"],
    "translate": ["แปล", "translate", "ภาษา", "แปลว่า"],
    "summarise": ["สรุป", "ย่อ", "ใจความ", "สรุปให้", "สรุปว่า"],
    "chat": [],  # fallback — no keywords needed
}

MODEL_MAP = {
    "weather":   "typhoon",   # formats Thai weather reply
    "translate": "qwen",      # fast, multilingual
    "summarise": "typhoon",   # better Thai NLP
    "chat":      "qwen",      # fast general chat
}

def route(text: str) -> dict:
    """
    Takes a Thai text string.
    Returns a dict with the task and which model to use.

    Example:
        route("ช่วยสรุปข่าวนี้หน่อย")
        → {"task": "summarise", "model": "typhoon"}
    """
    text_lower = text.lower()

    # Stage 1: scan for keywords
    for task, keywords in KEYWORD_MAP.items():
        for word in keywords:
            if word in text_lower:
                return {
                    "task": task,
                    "model": MODEL_MAP[task],
                    "stage": "keyword"   # tells us how decision was made
                }

    # No keyword matched → default to fast chat
    return {
        "task": "chat",
        "model": "qwen",
        "stage": "fallback"
    }