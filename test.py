from llama_cpp import Llama

print("Loading Typhoon...")

model = Llama(
    model_path="./models/llama3.2-typhoon2-t1-3b-q4_k_m.gguf",
    n_ctx=512,
    verbose=False,
    chat_format="chatml"
)

print("Testing Thai...")

response = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "คุณคือ Kuppi ผู้ช่วยส่วนตัวภาษาไทย ตอบกลับเป็นภาษาไทยเสมอ"
        },
        {
            "role": "user",
            "content": "สวัสดี วันนี้อากาศเป็นยังไงบ้าง"
        }
    ]
)

print(response["choices"][0]["message"]["content"])