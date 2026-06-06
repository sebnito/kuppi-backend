from llm.model_manager import ModelManager
from llm.kuppi_personality import build_prompt

manager = ModelManager()

def ask(model_name: str, user_input: str, stream: bool = False):

    manager.load_model(model_name)
    prompt = build_prompt(user_input)

    if stream:
        print("Kuppi: ", end="", flush=True)

        full_text = ""
        
        for chunk in manager.generate(prompt, stream=True):
            print(chunk)
            token = chunk["choices"][0]["text"]
            print(token, end="", flush=True)
            full_text += token

        print()  # new line when done
        return full_text
    else:
        result = manager.generate(prompt, stream=False)
        print(f"Kuppi: {result['text']}")
        return result["text"]

if __name__ == "__main__":
    while True:
        model_name = input("Choose a model (e.g., 'typhoon', 'qwen'): ")
        user_input = input("You: ")
        if user_input.lower() in {"exit"}:
            print("Goodbye!")
            break

        response = ask(model_name, user_input, stream=True)
        print(response)